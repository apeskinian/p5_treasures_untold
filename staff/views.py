from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from support.models import Faqs
from support.forms import FaqsForm
from products.models import Product
from products.forms import ProductForm


@staff_member_required
def dashboard(request):
    """
    a dashboard for staff where they can manage site related admin
    """
    faqs = Faqs.objects.all()
    products = Product.objects.all()

    active_tab = request.GET.get('tab')

    template = 'staff/dashboard.html'
    context = {
        'faqs': faqs,
        'products': products
    }

    if not context.get('active_tab'):
        context['active_tab'] = active_tab or 'Product'

    return render(request, template, context)


@staff_member_required
def manage_faq(request, delete=None, faq_id=None):
    """
    add, update or delete a faq
    """
    faqs = Faqs.objects.all()
    mode = 'Delete' if delete and faq_id else 'Update' if faq_id else 'Add'
    return_url = f"{reverse('dashboard')}?tab=FAQ"
    faq = None

    if faq_id:
        faq = get_object_or_404(Faqs, pk=faq_id)

    if request.method == 'POST':
        if delete:
            try:
                faq.delete()
                messages.success(request, 'FAQ deleted')
                return redirect(return_url)
            except Exception as e:
                messages.error(request, f'Error deleting FAQ: {e}')
                return redirect(return_url)
        else:
            form = FaqsForm(request.POST, instance=faq)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'FAQ updated' if faq_id else 'FAQ Added'
                )
                return redirect(return_url)
            else:
                messages.error(
                    request,
                    'Failed to update FAQ' if faq_id else 'Failed to add FAQ'
                )
                return redirect(return_url)
    else:
        form = FaqsForm(instance=faq)

    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'FAQ',
        'faqs': faqs,
        'mode': mode,
        'return_url': return_url,
    }
    if mode == 'Delete':
        context['to_delete'] = faq
    else:
        context['form'] = form

    return render(request, template, context)


@staff_member_required
def manage_product(request, delete=None, product_id=None):
    """
    add, update or delete a product
    """
    products = Product.objects.all()
    mode = (
        'Delete' if delete and product_id else
        'Update' if product_id else 'Add'
    )
    return_url = f"{reverse('dashboard')}?tab=Product"
    product = None

    if product_id:
        product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        if delete:
            try:
                product.delete()
                messages.success(request, 'Product deleted')
                return redirect(return_url)
            except Exception as e:
                messages.error(request, f'Error deleting product: {e}')
                return redirect(return_url)
        else:
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Product updated' if product_id else 'Product Added'
                )
                return redirect(return_url)
            else:
                messages.error(
                    request,
                    'Failed to update product'
                    if product_id else 'Failed to add product'
                )
    else:
        form = ProductForm(instance=product)

    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'Product',
        'products': products,
        'mode': mode,
        'return_url': return_url,
    }
    if mode == 'Delete':
        context['to_delete'] = product
    else:
        context['form'] = form

    return render(request, template, context)
