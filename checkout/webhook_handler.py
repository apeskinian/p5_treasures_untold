from decimal import Decimal
import json
import time

import stripe

from django.conf import settings
from django.contrib.sessions.models import Session
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from products.models import Product
from profiles.models import UserProfile

from .models import Order, OrderLineItem


class StripeWH_Handler:
    """
    Handles incoming webhooks from Stripe.

    This class is designed to process events sent by Stripe to the server. It
    listens for webhook events, verifies the event, and performs appropriate
    actions based on the event type.
    """
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Sends a confirmation email to the user after a successful order.
        The email is constructed using context information from the instance of
        :model:`checkout.Order` that was passed and the email templates.

        **Arguments:**
        - `order`: Instance of :model:`checkout.Order` containing all the order
            details.

        **Context:**
        - `home_url`: Absolute URL to the home page.
        - `contact_url`: Absolute URL to the contact page.
        - `order_total`: The total amount for the order
            (formatted to 2 decimal places).
        - `order_original_total`: The original total before any discounts
            (formatted to 2 decimal places).
        - `order_delivery_cost`: The cost for delivery
            (formatted to 2 decimal places).
        - `order_grand_total`: The grand total for the order
            (formatted to 2 decimal places).
        - `customer_email`: The email address of the customer receiving the
            confirmation.

        **Template:**
        :template:`checkout/confirmation_emails/confirmation_email_subject.txt`
        :template:`checkout/confirmation_emails/confirmation_email_body.html`
        """
        # Set variables for method.
        home_url = self.request.build_absolute_uri(reverse('home'))
        contact_url = self.request.build_absolute_uri(reverse('contact'))
        order_total = "{:.2f}".format(order.order_total)
        order_original_total = "{:.2f}".format(
            (order.order_total) / Decimal(0.8)
        )
        order_delivery_cost = "{:.2f}".format(order.delivery_cost)
        order_grand_total = "{:.2f}".format(order.grand_total)
        customer_email = order.email

        # Construct email subject and body.
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        html_message = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.html',
            {
                'order': order,
                'home_url': home_url,
                'contact_url': contact_url,
                'order_total': order_total,
                'order_original_total': order_original_total,
                'order_delivery_cost': order_delivery_cost,
                'order_grand_total': order_grand_total
            }
        )
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            html_message=html_message
        )

    def handle_event(self, event):
        """
        Handle a generic webhook event.

        **Arguments:**
        - `event`: A dictionary containing the event data received from the
            webhook.

        **Returns:**
        - `HttpResponse`: A response indicating that the webhook was received
            and handled, with a status code of 200 for successful processing.
        """
        return HttpResponse(
            content=f"TU Unhandled webhook: {event['type']}", status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.

        This method processes the `payment_intent.succeeded` webhook event from
        Stripe, which indicates that a payment has been successfully processed.
        It retrieves the necessary order details, updates the user's profile
        with shipping information if the `save_info` flag is set, and either
        verifies an existing order or creates a new order in the database.
        Afterward, a confirmation email is sent to the user.

        **Arguments:**
        - `event`: The webhook event from Stripe, containing metadata about the
            payment intent and other relevant data (such as basket contents,
            rewards, and session key).

        **Process:**
        - Retrieves the payment intent and charge details from Stripe.
        - Checks if the user profile should be updated with the details.
        - Attempts to find an existing order in the database based on the
            payment details and shipping address.
        - If no existing order is found, creates a new order and assigns
            products, including applying rewards and discounts.
        - Sends a confirmation email to the user.
        - If a session key is present, updates the session data to remove
            basket and reward information.

        **Returns:**
        - `HttpResponse`:
            - On success: A response indicating that the order was created or
                verified successfully.
            - On error: A response with a relevant error message (e.g., if a
                user is not found or a database error occurs).
        """
        # Set method variables.
        intent = event.data.object
        pid = intent.id
        basket_contents = intent.metadata.basket_contents
        active_rewards = intent.metadata.active_rewards
        session_key = intent.metadata.session_key
        save_info = intent.metadata.save_info

        # Getting the charge object.
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean the data for the shipping details.
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None
        if shipping_details.phone == '':
            shipping_details.phone = None

        # Update user profile information if save_info was checked.
        try:
            current_user = intent.metadata.current_user
            profile = UserProfile.objects.get(user__username=current_user)
            if save_info == 'true':
                profile.default_full_name = shipping_details.name
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address_1 = (
                    shipping_details.address.line1
                )
                profile.default_street_address_2 = (
                    shipping_details.address.line2
                )
                profile.default_town_city = shipping_details.address.city
                profile.default_county = shipping_details.address.state
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.save()
        except UserProfile.DoesNotExist:
            return HttpResponse(
                    content='User not found, database error',
                    status=500
                )

        # Look for order created by views.py
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address_1__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    town_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_basket=basket_contents,
                    rewards_used=active_rewards,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content='Order verified in database', status=200
            )
        else:
            # Order not found so proceed to create order here.
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address_1=shipping_details.address.line1,
                    street_address_2=shipping_details.address.line2,
                    town_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    grand_total=grand_total,
                    original_basket=basket_contents,
                    rewards_used=active_rewards,
                    stripe_pid=pid,
                )

                # Iterate through basket and apply reward discounts if and
                # where appropriate, then save line item.
                for index, (item_id, quantity) in enumerate(
                    json.loads(basket_contents).items()
                ):
                    product = Product.objects.get(pk=item_id)
                    if (
                        index < 3
                        and 'magic-lamp' in json.loads(active_rewards)
                    ):
                        product.price = 0
                    if (
                        product.realm
                        and product.realm.name == 'Agrabah'
                        and 'cave-of-wonders' in json.loads(active_rewards)
                    ):
                        product.price = 0
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        purchase_price=product.price,
                        quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f': {event['type']} | ERROR: {e}',
                    status=500
                )

        # Check for Bibbidi-Bobbidi-Boo reward.
        if 'bibbidi-bobbidi-boo' in json.loads(active_rewards):
            order.order_total *= Decimal(0.8)
            order.grand_total = (
                order.order_total + order.delivery_cost
            )
            order.save()

        # Send confirmation email.
        self._send_confirmation_email(order)

        # Clean up session data.
        if session_key:
            try:
                session = Session.objects.get(session_key=session_key)
                session_data = session.get_decoded()

                session_data.pop('basket', None)
                session_data.pop('rewards', None)

                session.session_data = Session.objects.encode(session_data)
                session.save()
                return HttpResponse(
                    content=f'TU Webhook received: {event['type']} | '
                    'SUCCESS order created in webhook.', status=200
                )
            except Session.DoesNotExist:
                return HttpResponse(
                    content=f'TU Webhook received: {event['type']} | '
                    'SUCCESS order created in webhook. '
                    'WARNING basket not cleared contact admin.', status=200
                )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe

        **Arguments:**
        - `event`: A dictionary containing the event data received from the
            webhook.

        **Returns:**
        - `HttpResponse`: A response indicating that the webhook was received
            and handled, with a status code of 200 for successful processing.
        """
        return HttpResponse(
            content=f"TU Payment failed: {event['type']}", status=200
        )
