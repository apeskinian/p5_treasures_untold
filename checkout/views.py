from decimal import Decimal
import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.http import require_POST

import stripe

from basket.contexts import basket_contents
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .forms import OrderForm
from .models import Order, OrderLineItem


@require_POST
def cache_checkout_data(request):
    """
    Modifies the stripe payment intent metadata wih the following additions:
    - `basket_contents`: A json export of the session basket dictionary.
    - `active_rewards`: A json export of the session rewards list.
    - `session_key`: The current session key.
    - `save_info`: The value from the checkbox in the checkout form.
    - `current_user`: The current user.

    **Raises:**
    - Exception: When the metadata fails to modify.

    **Returns:**
    - `HttpResponse` with status 200 on succesful modification.
    - `HttpResponse` with status 400 on failed modification.
    """
    # Add session and other relevant data to the stripe metadata.
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket_contents': json.dumps(request.session.get('basket', {})),
            'active_rewards': json.dumps(request.session.get('rewards', [])),
            'session_key': request.session.session_key,
            'save_info': request.POST.get('save_info'),
            'current_user': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment cannot be \
            processed right now. Please try again later')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    """
    Displays the checkout page, handles the checkout process, and creates an
    order.

    This view handles:
    - Collecting form data for the order.
    - Creating and saving an order, including associated line items.
    - Modifying the order total based on rewards applied.
    - Creating a Stripe payment intent for the checkout process.
    - Displaying appropriate messages for errors or success.

    **If the form is valid:**
    - An order is created with details from the form and session data.
    - Order line items are created for each product in the basket.
    - Relevant rewards (such as discounts) are applied to the order total.
    - A Stripe payment intent is generated for the user.

    **If the form is invalid:**
    - An error message is shown, and the user is prompted to correct their
        information.

    **Session Data Modified:**
    - The session is updated to indicate whether the user wants to save their
        information for future use.

    **Raises:**
    - `Product.DoesNotExist`: If a product in the basket cannot be found in the
        database.

    **Context:**
    - `order_form`: :form:`forms.OrderForm` instance.
    - `stripe_public_key`: Stripe public key from environment variables.
    - `client_secret`: Stripe payment intent.

    **Template:**
    - :template:`checkout/checkout.html`

    **Returns:**
    - Redirects to the checkout success page upon successful order creation.
    - Redirects to the basket view if the basket is empty or there's an error
        with the form.
    """
    # Set variables for method.
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Handling submission of order.
    if request.method == 'POST':
        basket = request.session.get('basket', {})
        rewards = request.session.get('rewards', [])

        # Collecting form data.
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'town_city': request.POST['town_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'phone_number': request.POST['phone_number']
        }

        # Process form
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.rewards_used = json.dumps(rewards)
            order.save()

            # Iterate through basket and apply reward discounts if and where
            # appropriate, then save line item.
            for index, (item_id, quantity) in enumerate(basket.items()):
                try:
                    product = get_object_or_404(Product, pk=item_id)
                    if index < 3 and 'magic-lamp' in rewards:
                        product.price = 0
                    if (
                        product.realm.name == 'Agrabah'
                        and 'cave-of-wonders' in rewards
                    ):
                        product.price = 0
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        purchase_price=product.price,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        'One of the products in the basket was lost fom our'
                        ' database. Please contact us for assistance'
                    ))
                    order.delete()
                    return redirect(reverse('view_basket'))
            request.session['save_info'] = 'save-info' in request.POST

            # Check for Bibbidi-Bobbidi-Boo reward
            if 'bibbidi-bobbidi-boo' in rewards:
                order.order_total *= Decimal(0.8)
                order.grand_total = (
                    order.order_total + order.delivery_cost
                )
                order.save()

            return redirect(
                reverse('checkout_success', args=[order.order_number])
            )
        else:
            messages.error(request, 'There was an error with your form. \
                           Please double check your information.')
    else:
        # Get basket contents and generate payment intent for Stripe.
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(
                request, "There's nothing in your basket at the moment"
            )
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    # Prefilling the checkout form from use profile saved info.
    try:
        profile = UserProfile.objects.get(user=request.user)
        order_form = OrderForm(initial={
            'full_name': profile.default_full_name,
            'email': profile.user.email,
            'phone_number': profile.default_phone_number,
            'street_address_1': profile.default_street_address_1,
            'street_address_2': profile.default_street_address_2,
            'town_city': profile.default_town_city,
            'county': profile.default_county,
            'postcode': profile.default_postcode,
            'country': profile.default_country,
        })
    except UserProfile.DoesNotExist:
        order_form = OrderForm()

    # Set up view parameters
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    """
    Handles the successful completion of a checkout, including updating the
    user's profile with the order information and clearing the session basket
    and rewards.

    This view:
    - Retrieves the order using the order number.
    - Updates the order with the user's profile data.
    - Saves the user's default shipping details if the user opted to save them.
    - Sends a success message and confirms the order.
    - Clears the basket and rewards session data.

    **If the user opted to save their info:**
    - The order details are used to update the user profile.
    - The user profile form is validated and saved.

    **Session Data Modified:**
    - The session basket and rewards are cleared upon successful checkout.

    **Raises:**
    - `Order.DoesNotExist`: If the order number provided does not exist.
    - `UserProfile.DoesNotExist`: If the user does not have a profile
        associated with their account.

    **Context:**
    - `order`: Instance of :model:`checkout.Order` that was processed.

    **Template:**
    - :template:`checkout/checkout_success.html`

    **Returns:**
    - Renders the `checkout_success.html`.
    """
    # Set variables for method.
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    profile = UserProfile.objects.get(user=request.user)
    order.user_profile = profile
    order.save()

    # Check if user requested to save the info provided.
    if save_info:
        profile_data = {
            'default_full_name': order.full_name,
            'default_phone_number': order.phone_number,
            'default_street_address_1': order.street_address_1,
            'default_street_address_2': order.street_address_2,
            'default_town_city': order.town_city,
            'default_postcode': order.postcode,
            'default_county': order.county,
            'default_country': order.country,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid:
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
                     Your order number is {order_number}. \
                        A confirmation email will be sent to you.')

    # Clear relevant session data.
    if 'basket' in request.session:
        del request.session['basket']
    if 'rewards' in request.session:
        del request.session['rewards']

    # Set up view parameters
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
