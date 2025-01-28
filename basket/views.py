from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product


def view_basket(request):
    """
    A view to show the basket contents
    """

    template = 'basket/basket.html'

    return render(request, template)


def add_to_basket(request, item_id):
    """
    Adds items to the basket
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    # update product stock level
    product = get_object_or_404(Product, pk=item_id)
    product.stock -= quantity
    product.save()

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the basket
    """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id, None)

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Removes an item from the basket
    """
    print('VIEWS TURN')
    basket = request.session.get('basket', {})
    quantity = int(request.POST['quantity'])
    print(quantity)

    # update product stock level
    product = get_object_or_404(Product, pk=item_id)
    product.stock += quantity
    product.save()

    basket.pop(item_id, None)
    request.session['basket'] = basket

    return redirect(reverse('view_basket'))
