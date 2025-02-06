from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower, TruncDate
from .models import Product, Realm
from .forms import ProductForm
from django.contrib.admin.views.decorators import staff_member_required


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


@staff_member_required
def add_product(request):
    """
    adds a new product to the shop
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product, please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@staff_member_required
def edit_product(request, product_id):
    """
    edits a product in the shop
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} successfully updated.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Error in updating product, please ensure form is valid'
            )
    else:
        form = ProductForm(instance=product)

    messages.info(request, f'Editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@staff_member_required
def delete_product(request, product_id):
    """
    deletes a product in the shop
    """
    product = get_object_or_404(Product, pk=product_id)
    try:
        product.delete()
        messages.success(request, 'Product deleted')
    except Exception:
        messages.error(request, 'Error deleting product')

    return redirect(reverse('products'))
