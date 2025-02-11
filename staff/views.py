from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from support.models import Faqs
from support.forms import FaqsForm


@staff_member_required
def dashboard(request):
    """
    a dashboard for staff where they can manage site related admin
    """
    faqs = Faqs.objects.all()

    active_tab = request.GET.get('tab')

    template = 'staff/dashboard.html'
    context = {
        'faqs': faqs,
    }

    if not context.get('active_tab'):
        context['active_tab'] = active_tab or 'Products'

    return render(request, template, context)


@staff_member_required
def manage_faq(request, delete=None, faq_id=None):
    """
    add or edit a faq
    """
    faqs = Faqs.objects.all()
    mode = 'Update' if faq_id else 'Add'
    return_url = f"{reverse('dashboard')}?tab=FAQ"
    faq = None

    if faq_id:
        faq = get_object_or_404(Faqs, pk=faq_id)

    if request.method == 'POST':
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
    else:
        form = FaqsForm(instance=faq)

    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'FAQ',
        'faqs': faqs,
        'form': form,
        'mode': mode,
        'return_url': return_url
    }
    print(context)

    return render(request, template, context)


@staff_member_required
def delete_faq(request, faq_id):
    """
    deletes a faq
    """
    faqs = Faqs.objects.all()
    faq = get_object_or_404(Faqs, pk=faq_id)
    return_url = f"{reverse('dashboard')}?tab=FAQ"
    if request.method == 'POST':
        try:
            faq.delete()
            messages.success(request, 'FAQ deleted')
            return redirect(return_url)
        except Exception as e:
            messages.error(request, f'Error deleting FAQ: {e}')
            return redirect(return_url)
    else:
        template = 'staff/dashboard.html'
        context = {
            'active_tab': 'FAQ',
            'faq_to_delete': faq,
            'faqs': faqs,
            'return_url': return_url
        }

    return render(request, template, context)
