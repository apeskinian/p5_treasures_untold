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
def add_faq(request):
    """
    adds a new faq
    """
    faqs = Faqs.objects.all()
    if request.method == 'POST':
        form = FaqsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ')
            return redirect(reverse('dashboard') + '?tab=faq')
        else:
            messages.error(
                request,
                'Failed to add new FAQ, please ensure the form is valid.'
            )
    else:
        form = FaqsForm()

    template = 'staff/dashboard.html'
    context = {
        'faqs': faqs,
        'faq_add_form': form,
        'active_tab': 'faq'
    }

    return render(request, template, context)


@staff_member_required
def edit_faq(request, faq_id):
    """
    edits a faq
    """
    faqs = Faqs.objects.all()
    faq = get_object_or_404(Faqs, pk=faq_id)
    if request.method == 'POST':
        form = FaqsForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ successfully updated.')
            return redirect(reverse('dashboard') + '?tab=faq')
        else:
            messages.error(
                request,
                'Error updating FAQ, please ensure the form is valid'
            )
    else:
        form = FaqsForm(instance=faq)

    template = 'staff/dashboard.html'
    context = {
        'faqs': faqs,
        'faq_edit_form': form,
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
