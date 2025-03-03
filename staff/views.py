from datetime import date, timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags

from products.forms import ProductForm, RealmForm
from products.models import Product, Realm
from support.forms import (
    FaqsForm, ContactReplyForm, NewsletterForm, FaqsTopicsForm
)
from support.models import (
    Faqs, ContactMessage, Subscriber, Newsletter, FaqsTopics
)


def getSubscribers():
    expiration_time = timezone.now() - timedelta(days=1)
    active_subscribers = Subscriber.objects.filter(is_active=True)
    unconfirmed_subscribers = Subscriber.objects.filter(
        is_active=False,
        date_joined__isnull=True,
        token_created_at__gte=expiration_time
    )
    expired_subscribers = Subscriber.objects.filter(
        is_active=False,
        date_joined__isnull=True,
        token_created_at__lt=expiration_time
    )
    return (active_subscribers, unconfirmed_subscribers, expired_subscribers)


def sendMessageReplyEmail(message_reply, request):
    """
    send the user an email with the reply created from the staff dashbpoard
    """
    email = message_reply.email
    home_url = request.build_absolute_uri(reverse('home'))
    subject = render_to_string(
        'staff/staff_emails/contact_reply_subject.txt',
        {'ticket': message_reply.ticket_number}
    )
    html_message = render_to_string(
        'staff/staff_emails/contact_reply_body.html',
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


def send_newsletter(new_newsletter, request):
    """
    Send the latest newsletter to all active subscribers including a link
    to unsubscribe.
    """
    subscribers = getSubscribers()[0]
    home_url = request.build_absolute_uri(reverse('home'))

    for subscriber in subscribers:
        email = subscriber.email
        unsubscribe_url = (
            request.build_absolute_uri(reverse(
                'confirm_unsubscription',
                args=[subscriber.id, subscriber.token]
            ))
        )
        subject = render_to_string(
            'staff/staff_emails/newsletter_subject.txt',
            {
                'date_sent': new_newsletter.date_sent
            }
        )
        html_message = render_to_string(
            'staff/staff_emails/newsletter_body.html',
            {
                'news_body': new_newsletter.news_body,
                'unsubscribe_url': unsubscribe_url,
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

    messages.success(request, 'Newsletter sent to all subscribers')


@staff_member_required
def dashboard(request):
    """
    a dashboard for staff where they can manage site related admin
    """
    active_subscribers, unconfirmed_subscribers, expired_subscribers = (
        getSubscribers()
    )
    faqs = Faqs.objects.all()
    faq_topics = FaqsTopics.objects.all()
    products = Product.objects.all()
    contact_messages = ContactMessage.objects.all()
    newsletters = Newsletter.objects.all()

    active_tab = request.GET.get('tab')

    template = 'staff/dashboard.html'
    context = {
        'faqs': faqs,
        'faq_topics': faq_topics,
        'products': products,
        'contact_messages': contact_messages,
        'active_subscribers': active_subscribers,
        'unconfirmed_subscribers': unconfirmed_subscribers,
        'expired_subscribers': expired_subscribers,
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
def manage_faq_topic(request, delete=None, faq_topic_id=None):
    """
    add, update or delete a faq tpoic
    """
    faq_topics = FaqsTopics.objects.all()
    mode = (
        'Delete' if delete and faq_topic_id else
        'Update' if faq_topic_id else 'Add'
    )
    return_url = f"{reverse('dashboard')}?tab=FAQ"
    faq_topic = None

    if faq_topic_id:
        faq_topic = get_object_or_404(FaqsTopics, pk=faq_topic_id)

    if request.method == 'POST':
        if delete:
            try:
                faq_topic.delete()
                messages.success(request, 'FAQ topic deleted')
                return redirect(return_url)
            except Exception as e:
                messages.error(request, f'Error deleting FAQ topic: {e}')
                return redirect(return_url)
        else:
            form = FaqsTopicsForm(request.POST, instance=faq_topic)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'FAQ topic updated' if faq_topic_id else 'FAQ topic Added'
                )
                return redirect(return_url)
            else:
                messages.error(
                    request,
                    'Failed to update FAQ topic' if faq_topic_id else
                    'Failed to add FAQ topic'
                )
                return redirect(return_url)
    else:
        form = FaqsTopicsForm(instance=faq_topic)

    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'FAQ Topic',
        'faq_topics': faq_topics,
        'mode': mode,
        'return_url': return_url,
        'title': 'Staff Dashboard'
    }
    if mode == 'Delete':
        context['to_delete'] = faq_topic
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
def manage_realm(request, delete=None, realm_id=None):
    """
    add, update or delete a realm
    """
    products = Product.objects.all()
    mode = (
        'Delete' if delete and realm_id else
        'Update' if realm_id else 'Add'
    )
    return_url = f"{reverse('dashboard')}?tab=Product"
    realm = None

    if realm_id:
        realm = get_object_or_404(Realm, pk=realm_id)

    if request.method == 'POST':
        if delete:
            try:
                realm.delete()
                messages.success(request, 'Realm deleted')
                return redirect(return_url)
            except Exception as e:
                messages.error(request, f'Error deleting realm: {e}')
                return redirect(return_url)
        else:
            if realm_id:
                form = RealmForm(request.POST, instance=realm)
            else:
                new_realm_name = request.POST['name'].replace(' ', '_')
                form = RealmForm({'name': new_realm_name})
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Realm updated' if realm_id else 'Realm created'
                )
                return redirect(return_url)
            else:
                messages.error(
                    request,
                    'Failed to update realm'
                    if realm_id else 'Failed to create realm'
                )
    else:
        form = RealmForm(instance=realm)

    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'Realm',
        'products': products,
        'mode': mode,
        'return_url': return_url,
        'title': 'Staff Dashboard'
    }
    if mode == 'Delete':
        context['to_delete'] = realm
    else:
        context['form'] = form

    return render(request, template, context)


@staff_member_required
def reply_to_message(request, message_id):

    contact_messages = ContactMessage.objects.all()
    mode = 'Reply'
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
def manage_newsletters(request, delete=None, newsletter_id=None):
    """
    Send a simple newsletter, view previously sent newsletters and delete
    previous newsletters
    """
    newsletters = Newsletter.objects.all()
    active_subscribers, unconfirmed_subscribers, expired_subscribers = (
        getSubscribers()
    )
    mode = (
        'Delete' if delete and newsletter_id else
        'View' if newsletter_id else 'Send'
    )
    return_url = f"{reverse('dashboard')}?tab=Newsletter"
    newsletter = None

    if newsletter_id:
        newsletter = get_object_or_404(Newsletter, pk=newsletter_id)

    if request.method == 'POST':
        if delete:
            try:
                newsletter.delete()
                messages.success(request, 'Newsletter deleted')
                return redirect(return_url)
            except Exception as e:
                messages.error(request, f'Error deleting newsletter: {e}')
                return redirect(return_url)
        else:
            form = NewsletterForm(request.POST, instance=newsletter)
            if form.is_valid:
                new_newsletter = form.save()
                send_newsletter(new_newsletter, request)
                messages.success(request, 'Newsletter created')
            else:
                messages.error(
                    request,
                    'Failed to create newsletter, ensure form is valid')
            return redirect(return_url)
    else:
        form = NewsletterForm(instance=newsletter)

    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'Newsletter',
        'active_subscribers': active_subscribers,
        'unconfirmed_subscribers': unconfirmed_subscribers,
        'expired_subscribers': expired_subscribers,
        'newsletters': newsletters,
        'mode': mode,
        'return_url': return_url,
        'title': 'Staff Dashboard'
    }
    if mode == 'Delete':
        context['to_delete'] = newsletter
    else:
        context['form'] = form

    return render(request, template, context)


@staff_member_required
def manage_subscriber(request, subscriber_id):
    """
    Removes a subscriber from the newsletter recipients
    """
    active_subscribers, unconfirmed_subscribers, expired_subscribers = (
        getSubscribers()
    )
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
        'active_subscribers': active_subscribers,
        'unconfirmed_subscribers': unconfirmed_subscribers,
        'expired_subscribers': expired_subscribers,
        'newsletters': newsletters,
        'mode': mode,
        'return_url': return_url,
        'to_delete': subscriber,
        'title': 'Staff Dashboard'
    }

    return render(request, template, context)


@staff_member_required
def clear_expired_subscribers(request):
    active_subscribers, unconfirmed_subscribers, expired_subscribers = (
        getSubscribers()
    )
    expired_subscribers = getSubscribers()[2]
    newsletters = Newsletter.objects.all()
    mode = 'Clear'
    return_url = f"{reverse('dashboard')}?tab=Newsletter"

    if request.method == 'POST':
        if expired_subscribers.exists():
            expired_subscribers.delete()
            messages.success(request, 'All expired subscribers removed')
        else:
            messages.error(request, 'There are no expired subscribers')
        return redirect(return_url)

    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'Newsletter',
        'active_subscribers': active_subscribers,
        'unconfirmed_subscribers': unconfirmed_subscribers,
        'expired_subscribers': expired_subscribers,
        'newsletters': newsletters,
        'mode': mode,
        'return_url': return_url,
        'to_delete': expired_subscribers,
        'title': 'Staff Dashboard'
    }

    return render(request, template, context)
