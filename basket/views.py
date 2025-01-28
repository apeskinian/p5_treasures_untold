from django.shortcuts import render, redirect, reverse


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
    basket = request.session.get('basket', {})
    basket.pop(item_id, None)
    request.session['basket'] = basket

    return redirect(reverse('view_basket'))
