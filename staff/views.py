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

    template = 'staff/dashboard.html'
    context = {
        'faqs': faqs,
        'active_tab': 'faq'
    }

    return render(request, template, context)


@staff_member_required
def manage_faq(request, faq_id=None):
    """
    add or edit a faq
    """
    faqs = Faqs.objects.all()

    if request.method == 'POST':
        if faq_id:
            faq = get_object_or_404(Faqs, pk=faq_id)
            form = FaqsForm(request.POST, instance=faq)
        else:
            form = FaqsForm(request.POST)

        if form.is_valid():
            form.save()
            if faq_id:
                messages.success(request, 'FAQ updated')
            else:
                messages.success(request, 'FAQ added')
        else:
            if faq_id:
                messages.error(
                    request,
                    'Failed to update FAQ, please ensure form is valid'
                )
            else:
                messages.error(
                    request,
                    'Failed to add FAQ, please ensure form is valid'
                )
        return redirect(reverse('dashboard')+'?tab=faq')
    else:
        if faq_id:
            faq = get_object_or_404(Faqs, pk=faq_id)
            form = FaqsForm(instance=faq)
        else:
            form = FaqsForm()

        template = 'staff/dashboard.html'
        context = {
            'faqs': faqs,
            'faq_edit_form' if faq_id else 'faq_add_form': form,
            'active_tab': 'faq'
        }

        return render(request, template, context)


@staff_member_required
def delete_faq(request, faq_id):
    """
    deletes a faq
    """
    faqs = Faqs.objects.all()
    faq = get_object_or_404(Faqs, pk=faq_id)
    if request.method == 'POST':
        try:
            faq.delete()
            messages.success(request, 'FAQ deleted')
            return redirect(reverse('dashboard') + '?tab=faq')
        except Exception as e:
            messages.error(request, f'Error deleting FAQ: {e}')
            return redirect(reverse('dashboard') + '?tab=faq')
    else:
        template = 'staff/dashboard.html'
        context = {
            'faq_to_delete': faq,
            'faqs': faqs,
            'active_tab': 'faq'
        }

    return render(request, template, context)
