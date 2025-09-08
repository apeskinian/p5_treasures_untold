import os
import random

from django.db.models.functions import TruncDate
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_control

from products.models import Product, Realm
from profiles.models import UserProfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    """
    A view to return the index page including a queryset for the newest
    products added to the store and one for a featured realm which is randomly
    picked on each page load.

    **Arguments:**
    - `request`: The HTTP request.

    **Context:**
    - `current_user`: The current user if logged in.
    - `new_products`: queryset of :model:`products.Product` filtered to include
        the newest products added.
    - `featured_realm`: queryset of :model:`products.Realm` chosen at random.
    - `featured_products`: queryset of :model:`products.Product` filtered to
        include products from the featured realm.

    **Template:**
    - :template:`home/index.html`

    **Returns:**
    - A render response showing the homepage.
    """
    # Getting username if logged in.
    current_user = None
    if request.user.is_authenticated:
        current_user = get_object_or_404(UserProfile, user=request.user)

    # Getting items for new section.
    most_recent_dates = (
        Product.objects.annotate(added_date=TruncDate('date_added'))
        .values('added_date')
        .distinct()
        .order_by('-added_date')[:1]
    )
    if most_recent_dates:
        new_products = (
            Product.objects.filter(
                date_added__in=[
                    date['added_date'] for date in most_recent_dates
                ]
            )
        )
    else:
        new_products = Product.objects.none()

    # Get a realm to feature and create queryset but pick again if the
    # realm has no products.
    featured_products = Product.objects.none()
    while featured_products.count() < 1:
        realm_count = Realm.objects.count()
        random_index = random.randint(0, realm_count - 1)
        featured_realm = Realm.objects.all()[random_index]
        featured_products = Product.objects.filter(realm=featured_realm)

    # Setting up view parameters.
    template = 'home/index.html'
    context = {
        'current_user': current_user,
        'new_products': new_products,
        'featured_realm': featured_realm,
        'featured_products': featured_products
    }

    return render(request, template, context)


def robots_txt(request):
    return FileResponse(
        open(os.path.join(BASE_DIR, 'home/static/home/robots.txt'), 'rb'),
        content_type='text/plain'
    )


def sitemap_xml(request):
    return FileResponse(
        open(os.path.join(BASE_DIR, 'home/static/home/sitemap.xml'), 'rb'),
        content_type='application/xml'
    )
