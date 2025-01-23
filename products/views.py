from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Realm


def all_products(request):
    """
    A view to show all products including sorting and search queries
    """
    products = Product.objects.all()
    query = None
    realms = None

    if request.GET:

        if 'realm' in request.GET:
            realms = request.GET['realm'].split(',')
            products = products.filter(realm__name__in=realms)
            realms = Realm.objects.filter(name__in=realms)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "Your spell needs a little more magic, "
                    "enter search criteria to begin!"
                )
                return redirect(reverse('products'))
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            products = products.filter(queries)

    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'current_realms': realms,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """
    A view to show a single product in more detail
    """
    product = get_object_or_404(Product, pk=product_id)

    template = 'products/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, template, context)
