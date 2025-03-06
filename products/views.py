from django.db.models import Q, Case, When, Value, IntegerField
from django.db.models.functions import Lower, TruncDate
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Product, Realm


def all_products(request):
    """
    A view to display all products with sorting, searching, and filtering
    options.

    **Arguments:**
    - `request`: The HTTP request object containing GET parameters for sorting,
      filtering, and search criteria.

    **Context:**
    - `products`: A queryset of :model:`products.Product`, filtered and sorted
      based on the request parameters.
    - `search_term`: A string containing the user input from the search bar.
    - `current_realms`: A queryset of :model:`products.Realm` based on the
        selected realm filter from the request.
    - `current_realms_names`: A list of realm names derived from the selected
      realms.
    - `current_sorting`: A string representing the current sorting key and
        direction.
    - `showing_new`: A boolean indicating if only new products are being shown.
    - `showing_stock`: A list indicating whether the stock filter is set to
        'in' or 'out' of stock.

    **Template:**
    - :template:`products/products.html`

    **Returns:**
    - A rendered response displaying the filtered and sorted products based on
        the request parameters.
    """
    # Set up variables for method.
    products = Product.objects.annotate(
        in_stock=Case(
            When(stock=0, then=Value(1)),
            default=Value(0),
            output_field=IntegerField(),
        )
    ).order_by('in_stock', 'realm__name')
    query = None
    realms = None
    sort = None
    direction = None
    showing_new = False
    showing_stock = None
    current_realms_names = None
    showing_stock = []
    return_url = request.META.get('HTTP_REFERER')

    # Handling GET parameters.
    if request.GET:
        # Looking for latest additions query.
        if 'new' in request.GET:
            showing_new = True
            most_recent_dates = (
                Product.objects.annotate(added_date=TruncDate('date_added'))
                .values('added_date')
                .distinct()
                .order_by('-added_date')[:1]
            )
            if most_recent_dates:
                products = (
                    Product.objects.filter(
                        date_added__in=[
                            date['added_date'] for date in most_recent_dates
                        ]
                    )
                )
            else:
                products = Product.objects.none()
        # Looking for product sorting.
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'realm':
                sortkey = 'realm__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        # Looking for stock filter.
        if 'stock' in request.GET:
            stock_requests = request.GET['stock'].split(',')
            in_stock_products = products.none()
            out_of_stock_products = products.none()
            if 'in' in stock_requests:
                in_stock_products = products.filter(stock__gt=0)
                showing_stock.append('in')
            if 'out' in stock_requests:
                out_of_stock_products = products.filter(stock__exact=0)
                showing_stock.append('out')
            products = in_stock_products | out_of_stock_products
        # Looking for realm filter.
        if 'realm' in request.GET:
            realms = request.GET['realm'].split(',')
            products = products.filter(realm__name__in=realms)
            realms = Realm.objects.filter(name__in=realms)
            current_realms_names = (
                realms.order_by('name').values_list('name', flat=True)
            )
        # Handling search bar queries.
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "Your spell needs a little more magic, "
                    "enter search criteria to begin!"
                )
                return redirect(reverse('products'))
            # Bibbidi-Bobbidi-Boo reward handling.
            if query.lower() == 'bibbidi-bobbidi-boo':
                if request.user.is_authenticated:
                    activate_reward(request, 'activate', 'bibbidi-bobbidi-boo')
                    return redirect(return_url)
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # Setting up view parameters
    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'current_realms': realms,
        'current_realms_names': current_realms_names,
        'current_sorting': current_sorting,
        'showing_new': showing_new,
        'showing_stock': showing_stock,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """
    A view to display detailed information for a single product.

    **Arguments:**
    - `request`: The HTTP request object.
    - `product_id`: The ID used to retrieve the instance of
        :model:`products.Product`.

    **Context:**
    - `product`: The instance of :model:`products.Product` corresponding to the
        provided `product_id`.
    - `return_url`: The URL for redirection. It first tries to retrieve this
        from the session's `return_url` key, removing it afterward. If not
        found, it uses `HTTP_REFERER`. As a final fallback, it redirects to the
        `products` view to avoid a potential HTTP_REFERER loop when the user
        adds an item to the basket.

    **Returns:**
    - A rendered response displaying the product detail page for the specified
        product.
    """
    # Set variables for method.
    product = get_object_or_404(Product, pk=product_id)
    return_url = request.session.pop(
        'return_url',
        request.META.get('HTTP_REFERER', reverse('products'))
    )

    # Setting up view parameters
    template = 'products/product_detail.html'
    context = {
        'product': product,
        'return_url': return_url
    }

    return render(request, template, context)


def activate_reward(request, action=None, reward=None, extra=None):
    """
    Activates or deactivates a reward and updates the session for processing at
    checkout.

    **Arguments:**
    - `request`: The HTTP request object.
    - `action`: A string that can be either 'activate' or 'deactivate' to
        indicate the desired reward action.
    - `reward`: A string containing the name of the reward to be activated or
        deactivated.
    - `extra`: An optional string for any additional arguments needed for the
        reward.

    **Returns:**
    - `HttpResponse`: A response with status 200 on successful actions.
    - `HttpResponse`: A response with status 404 if the reward is not found.
    """
    # Set up variables for the method.
    action = action if action else None
    reward = reward if reward else None

    # Handling no argument error.
    if not reward:
        return HttpResponse('reward not found', status=404)

    rewards = request.session.get('rewards', [])

    if action == 'activate' and reward not in rewards:
        rewards.append(reward)
        request.session['rewards'] = rewards
        messages.add_message(request, settings.REWARDSMESSAGE, reward)
        return HttpResponse('reward added', status=200)
    elif action == 'deactivate' and reward in rewards:
        rewards.remove(reward)
        request.session['rewards'] = rewards
        if extra:
            messages.add_message(request, settings.REWARDSMESSAGE, extra)
        return HttpResponse('reward removed', status=200)
    else:
        return HttpResponse('no changes', status=200)
