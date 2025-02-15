import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower, TruncDate
from .models import Product, Realm
from django.conf import settings


def all_products(request):
    """
    A view to show all products including sorting and search queries
    """
    products = Product.objects.all()
    query = None
    realms = None
    sort = None
    direction = None
    showing_new = False
    showing_stock = None
    current_realms_names = None
    showing_stock = []

    if request.GET:
        # looking for latest additions query
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
        # looking for product sorting
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
        # looking for stock filter
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
        # looking for realm filter
        if 'realm' in request.GET:
            realms = request.GET['realm'].split(',')
            products = products.filter(realm__name__in=realms)
            realms = Realm.objects.filter(name__in=realms)
            current_realms_names = (
                realms.order_by('name').values_list('name', flat=True)
            )
        # handling search bar queries
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "Your spell needs a little more magic, "
                    "enter search criteria to begin!"
                )
                return redirect(reverse('products'))
            # bibbidi-bobbidi-boo discount easter-egg
            if query.lower() == 'bibbidi-bobbidi-boo':
                if request.user.is_authenticated:
                    activate_reward(request, 'activate', 'bibbidi-bobbidi-boo')
                    return redirect(reverse('products'))
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # setting up view parameters
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
    A view to show a single product in more detail
    """
    product = get_object_or_404(Product, pk=product_id)

    # setting up view parameters
    template = 'products/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


def activate_reward(request, action=None, reward=None):
    """
    Handles reward activations and adds them to the session for processsing
    at checkout.
    """
    if reward:
        reward = reward
        action = action
    else:
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                reward = data.get('reward')
                action = data.get('action')
                if not reward:
                    return JsonResponse(
                        {'error': 'Reward not found in data'}, status=400
                    )
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
    if reward:
        rewards = request.session.get('rewards', [])
        if reward not in rewards and action == 'activate':
            rewards.append(reward)
            request.session['rewards'] = rewards
            request.session.modified = True
            messages.add_message(request, settings.REWARDSMESSAGE, reward)
            print(rewards)
            return JsonResponse({'message': f'Reward {reward} activated!'})
        elif reward in rewards and action == 'activate':
            messages.info(request, f'{reward} already activated')
            print(rewards)
            return JsonResponse({'message': f'Reward {reward} activated!'})
        elif reward in rewards and action == 'deactivate':
            rewards.remove(reward)
            request.session['rewards'] = rewards
            request.session.modified = True
            messages.info(request, f'{reward} deactivated')
            print(rewards)
            return JsonResponse({'message': f'Reward {reward} deactivated!'})
        else:
            messages.info(request, f'{reward} delete this message')
            print(rewards)
            return JsonResponse({'message': f'Reward {reward} deactivated!'})
    else:
        return JsonResponse({'error': 'Reward not specified'}, status=400)
