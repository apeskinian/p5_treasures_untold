from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    A view to show all products including sorting and search queries
    """
    products = Product.objects.all()

    template = 'products/products.html'
    context = {
        'products': products,
    }

    return render(request, template, context)
