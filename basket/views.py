from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404, HttpResponse, redirect, render, reverse
)

from products.models import Product
from products.views import activate_reward


def update_stock(request, product, adjustment):
    """
    Updates the stock level of a product. Called when adding, updating and
    deleting items in the basket.

    **Arguments:**
    - `request`: The HTTP request.
    - `product`: An instance of :model:`products.Product`.
    - `adjustment`: An integer value to apply to the stock level
        (positive or negative).

    **Raises:**
    - ValueError: If stock becomes negative or exceeds the limit for unique
        items.
    """
    try:
        updated_stock = product.stock
        updated_stock += adjustment
        if updated_stock < 0:
            raise ValueError('Stock cannot be negative')
        elif product.unique_stock and updated_stock > 1:
            raise ValueError(
                'Stock cannot be more than one for unique items'
            )
        else:
            product.stock += adjustment
            product.save()
    except ValueError:
        pass

    request.session.set_expiry(86400)


@login_required
def view_basket(request):
    """
    A view to show the basket contents.

    **Arguments:**
    - `request`: The HTTP request.

    **Template:**
    - :template:`basket/basket.html`

    **Returns:**
    - A rendered response with the basket template.
    """
    # Set up view parameters
    template = 'basket/basket.html'

    return render(request, template)


def add_to_basket(request, item_id):
    """
    Retrieves the basket data from the session and adds an item. If the item
    is already in the basket, the quantity is updated. Stock levels are also
    updated accordingly. The user is then redirected back to the page they were
    on.
    There is also a call to check for the `cave of wonders` reward.

    **Arguments:**
    - `request`: The HTTP request.
    - `item_id`: The ID of the product to be added to the basket.

    **Raises:**
    - Exception: If there is a problem in updating the basket or stock.

    **Returns:**
    - A redirect to the URL specified by `redirect_url`.
    """
    # Set up variables for the method
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    return_url = request.POST.get('return_url')
    basket = request.session.get('basket', {})

    # Create updated basket data.
    try:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(
                request,
                f'{product.name} quantity updated to {basket[item_id]}'
            )
        else:
            basket[item_id] = quantity
            messages.success(request, f'{product.name} added to basket')

        # Update product stock level
        update_stock(request, product, -quantity)
    except Exception as e:
        messages.error(
            request,
            f'There was a problem adding {product.name} to your basket: {e}'
            'Please try again later'
        )

    # Adjusting return_url to prevent loop.
    if return_url:
        request.session['return_url'] = return_url

    # Save basket data to session.
    request.session['basket'] = basket

    # Call to check for 'cave of wonders' reward.
    check_for_cave_of_wonders(request)

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjusts the quantity of an item in the basket. If the new quantity is
    set to 0, the item is removed from the basket. Stock levels are updated
    accordingly. The user is then redirected to the `view_basket` view.
    Additionally, it checks for the `cave of wonders` reward.

    **Arguments:**
    - `request`: The HTTP request.
    - `item_id`: The ID of the product to be adjusted in the basket.

    **Raises:**
    - Exception: If there is an issue updating the basket or stock levels.

    **Returns:**
    - A redirect to the `view_basket` view.
    """
    # Set up variables for the method
    product = get_object_or_404(Product, pk=item_id)
    previous_quantity = int(request.POST.get('previous-quantity'))
    new_quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    # Create updated basket data.
    try:
        if new_quantity > 0:
            basket[item_id] = new_quantity
            messages.success(
                request,
                f'{product.name} quantity updated to {basket[item_id]}'
            )
        else:
            basket.pop(item_id, None)
            messages.info(
                request, f'{product.name} removed from basket'
            )

        # Update product stock level
        quantity_delta = previous_quantity - new_quantity
        update_stock(request, product, quantity_delta)
    except Exception as e:
        messages.error(
            request,
            f'There was a problem adjusting {product.name} in your basket: {e}'
            'Please try again later'
        )

    # Save basket data to session.
    request.session['basket'] = basket

    # Call to check for 'cave of wonders' reward.
    check_for_cave_of_wonders(request)

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Removes an item from the basket and updates stock levels accordingly.
    Additionally, it checks for the `cave of wonders` reward.

    **Arguments:**
    - `request`: The HTTP request.
    - `item_id`: The ID of the product to be removed from the basket.

    **Raises:**
    - Exception: If there is an issue removing the item or updating stock
        levels.

    **Returns:**
    - A `HttpResponse` with status of 200 for a successul removal or 500 if an
        exception occurs.
    """
    # Remove the item from the basket
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        quantity = int(request.POST['quantity'])

        # Update product stock level
        update_stock(request, product, quantity)

        basket.pop(item_id, None)
        messages.info(
            request, f'{product.name} removed from basket'
        )
        request.session['basket'] = basket
        check_for_cave_of_wonders(request)
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def check_for_cave_of_wonders(request):
    """
    Checks the basket contents and determines whether to activate or deactivate
    the `Cave of Wonders` reward by calling `activate_reward`.

    **Conditions:**
    - **Activate**: Both halves of the Golden Scarab Beetle must be in the
        basket, and the Shiva Monkey Idol of Agrabah must NOT be in the basket.
    - **Deactivate**: If the Shiva Monkey Idol of Agrabah is added at any
        point, the reward is deactivated immediately, even if the scarab halves
        are present.

    **Arguments:**
    - `request`: The HTTP request.
    """
    # Set variables for method
    basket = request.session.get('basket', {})
    monkey_idol = str(get_object_or_404(Product, sku='TU-AGR-SMI-U').id)
    beetle_left = str(get_object_or_404(Product, sku='TU-AGR-LHGSB-U').id)
    beetle_right = str(get_object_or_404(Product, sku='TU-AGR-RHGSB-U').id)

    # Condition checking for reward activation/deactivation
    if monkey_idol not in basket.keys():
        if beetle_left in basket.keys() and beetle_right in basket.keys():
            activate_reward(request, 'activate', 'cave-of-wonders')
        else:
            activate_reward(request, 'deactivate', 'cave-of-wonders')
    elif monkey_idol in basket.keys():
        activate_reward(request, 'deactivate', 'cave-of-wonders', 'infidels')
