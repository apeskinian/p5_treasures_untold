from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QQ7P3KwFb8zfBaln98yb2yZFR0NEF4g5TJ2gHUFQAME2iLEvr791JgP12orn6UE1wek71rx5AhogIQvqDb7e37s00GHDiA5tL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
