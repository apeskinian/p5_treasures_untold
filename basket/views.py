from django.shortcuts import render


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
