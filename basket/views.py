from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product
from products.views import activate_reward


def update_stock(request, product, adjustment):
    """
    Update stock level of product
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
    A view to show the basket contents
    """
    # setting up view parameters
    template = 'basket/basket.html'

    return render(request, template)


def add_to_basket(request, item_id):
    """
    Adds items to the basket
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

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
        # update product stock level
        update_stock(request, product, -quantity)
    except Exception as e:
        messages.error(
            request,
            f'There was a problem adding {product.name} to your basket: {e}'
            'Please try again later'
        )

    request.session['basket'] = basket

    check_for_cave_of_wonders(request)

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the basket
    """
    product = get_object_or_404(Product, pk=item_id)
    previous_quantity = int(request.POST.get('previous-quantity'))
    new_quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

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
        # update product stock level
        quantity_delta = previous_quantity - new_quantity
        update_stock(request, product, quantity_delta)
    except Exception as e:
        messages.error(
            request,
            f'There was a problem adjusting {product.name} in your basket: {e}'
            'Please try again later'
        )

    request.session['basket'] = basket

    check_for_cave_of_wonders(request)

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Removes an item from the basket
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        quantity = int(request.POST['quantity'])

        # update product stock level
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

    basket = request.session.get('basket', {})
    monkey_idol = str(get_object_or_404(Product, sku='TU-AGR-SMI-U').id)
    beetle_left = str(get_object_or_404(Product, sku='TU-AGR-LHGSB-U').id)
    beetle_right = str(get_object_or_404(Product, sku='TU-AGR-RHGSB-U').id)

    if monkey_idol not in basket.keys():
        if beetle_left in basket.keys() and beetle_right in basket.keys():
            activate_reward(request, 'activate', 'cave-of-wonders')
        else:
            activate_reward(request, 'deactivate', 'cave-of-wonders')
    elif monkey_idol in basket.keys():
        activate_reward(request, 'deactivate', 'cave-of-wonders', 'infidels')
