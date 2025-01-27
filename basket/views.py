from django.shortcuts import render, redirect


def view_basket(request):
    """
    A view to show the basket contents
    """
    back_url = request.META.get('HTTP_REFERER')

    context = {
        'back_url': back_url
    }
    template = 'basket/basket.html'

    return render(request, template, context)


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
