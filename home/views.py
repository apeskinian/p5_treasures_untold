from django.shortcuts import render, get_object_or_404
from products.models import Product, Realm
from profiles.models import UserProfile
from django.db.models.functions import TruncDate
import random


def index(request):
    """
    A view to return the index page including a queryset for the newest
    products added to the store and one for a featured realm which
    is decided each week
    """
    current_user = None
    # getting username if logged in
    if request.user.is_authenticated:
        current_user = get_object_or_404(UserProfile, user=request.user)
    # getting items for new section
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

    # get a realm to feature and create queryset but pick again if the
    # realm has no products
    featured_products = Product.objects.none()
    while featured_products.count() < 1:
        realm_count = Realm.objects.count()
        random_index = random.randint(0, realm_count - 1)
        featured_realm = Realm.objects.all()[random_index]
        featured_products = Product.objects.filter(realm=featured_realm)

    # setting up view parameters
    template = 'home/index.html'
    context = {
        'current_user': current_user,
        'new_products': new_products,
        'featured_realm': featured_realm,
        'featured_products': featured_products,
    }

    return render(request, template, context)
