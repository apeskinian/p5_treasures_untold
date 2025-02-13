from datetime import date

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from support.models import Faqs, ContactMessage, Subscriber, Newsletter
from support.forms import FaqsForm, ContactReplyForm
from products.models import Product
from products.forms import ProductForm


def sendMessageReplyEmail(message_reply, request):
    """
    send the user an email with the reply created from the staff dashbpoard
    """
    email = message_reply.email
    home_url = request.build_absolute_uri(reverse('home'))
    subject = render_to_string(
        'staff/support_emails/contact_reply_subject.txt',
        {'ticket': message_reply.ticket_number}
    )
    html_message = render_to_string(
        'staff/support_emails/contact_reply_body.html',
        {
            'message': message_reply,
            'home_url': home_url
        }
    )
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        html_message=html_message
    )


@staff_member_required
def dashboard(request):
    """
    a dashboard for staff where they can manage site related admin
    """
    faqs = Faqs.objects.all()
    products = Product.objects.all()
    contact_messages = ContactMessage.objects.all()
    subscribers = Subscriber.objects.all()
    newsletters = Newsletter.objects.all()

    active_tab = request.GET.get('tab')

    template = 'staff/dashboard.html'
    context = {
        'faqs': faqs,
        'products': products,
        'contact_messages': contact_messages,
        'subscribers': subscribers,
        'newsletters': newsletters,
        'title': 'Staff Dashboard'
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
        'title': 'Staff Dashboard'
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
        'title': 'Staff Dashboard'
    }
    if mode == 'Delete':
        context['to_delete'] = product
    else:
        context['form'] = form

    return render(request, template, context)


@staff_member_required
def reply_to_message(request, message_id):

    contact_messages = ContactMessage.objects.all()
    mode = 'Reply to'
    return_url = f"{reverse('dashboard')}?tab=Message"
    message = get_object_or_404(ContactMessage, pk=message_id)

    if request.method == 'POST':
        form = ContactReplyForm(request.POST, instance=message)
        if form.is_valid:
            message.date_replied = date.today()
            message.replied = True
            message_reply = form.save()
            messages.success(request, 'Reply sent')
            sendMessageReplyEmail(
                message_reply,
                request,
            )
            return redirect(return_url)
        else:
            messages.error(
                request,
                'Failed to send reply, please ensure form is valid'
            )
    else:
        form = ContactReplyForm(instance=message)

    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'Message',
        'contact_messages': contact_messages,
        'mode': mode,
        'return_url': return_url,
        'form': form,
        'title': 'Staff Dashboard'
    }

    return render(request, template, context)


@staff_member_required
def staff_unsubscribe(request, subscriber_id):
    """
    Removes a subscriber from the newsletter recipients
    """
    subscribers = Subscriber.objects.all()
    newsletters = Newsletter.objects.all()
    mode = 'Unsubscribe'
    return_url = f"{reverse('dashboard')}?tab=Newsletter"
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)

    if request.method == 'POST':
        try:
            subscriber.delete()
            messages.success(request, 'Unsubscribed')
            return redirect(return_url)
        except Exception as e:
            messages.error(request, f'Error unsubscribing: {e}')
            return redirect(return_url)

    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'Newsletter',
        'subscribers': subscribers,
        'newsletters': newsletters,
        'mode': mode,
        'return_url': return_url,
        'to_delete': subscriber,
        'title': 'Staff Dashboard'
    }

    return render(request, template, context)
