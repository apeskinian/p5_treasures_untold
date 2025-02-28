import json
import time
from decimal import Decimal

import stripe

from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from profiles.models import UserProfile
from products.models import Product
from .models import Order, OrderLineItem


class StripeWH_Handler:
    """
    Handles webhooks from Stripe
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        sends the user a confirmation email
        """
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        """
        Handle a generic webhook event
        """
        return HttpResponse(
            content=f'TU Unhandled webhook: {event['type']}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket_contents = intent.metadata.basket_contents
        active_rewards = intent.metadata.active_rewards
        session_key = intent.metadata.session_key
        save_info = intent.metadata.save_info

        # getting the charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # clean the data for the shipping details
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        # update user profile information if save_info was checked
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
        except profile.DoesNotExist:
            return HttpResponse(
                    content='User not found, database error',
                    status=500
                )

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
                        product.realm.name == 'Agrabah'
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
                    content=f': {event['type']} | ERRROR: {e}',
                    status=500
                )

        if 'bibbidi-bobbidi-boo' in json.loads(active_rewards):
            order.order_total *= Decimal(0.8)
            order.grand_total = (
                order.order_total + order.delivery_cost
            )
            order.save()

        self._send_confirmation_email(order)

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
        """
        return HttpResponse(
            content=f'TU Payment failed: {event['type']}', status=200
        )
