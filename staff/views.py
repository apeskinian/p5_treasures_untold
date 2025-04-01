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
    """
    Retrieves and categorizes subscribers into three querysets based on their
    status.

    The expiration time for confirming email subscriptions is currently set to
    365 days for testing, though the email states a 24-hour confirmation
    period.

    **Returns:**
    - A queryset of active subscribers (`is_active=True`).
    - A queryset of unconfirmed subscribers (`is_active=False`,
        `date_joined__isnull=True`), where `token_created_at` is still valid
        (greater than the expiration time).
    - A queryset of expired subscribers (`is_active=False`,
        `date_joined__isnull=True`), where `token_created_at` has expired
        (less than the expiration time).
    """
    # Set expiration limit
    expiration_time = timezone.now() - timedelta(days=365)

    # Get querysets to return
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
    Sends an email reply to a contact message.
    The email is constructed using context information from the instance of
    :model:`support.ContactMessage` that was passed and the email templates.

    **Arguments:**
    - `message_reply`: An instance of :model:`support.ContactMessage`
        containing the reply content, recipient email, and ticket number.
    - `request`: The HTTP request used to build an absolute home page URL.

    **Context Data:**
    - `message_reply`: The contact reply instance.
    - `home_url`: Absolute URL to the home page.
    - `email`: The email address of the recipient.

    **Template:**
    :template:`staff/staff_emails/contact_reply_subject.txt`
    :template:`staff/staff_emails/contact_reply_body.html`
    """
    # Set variables for method.
    email = message_reply.email
    home_url = request.build_absolute_uri(reverse('home'))

    # Construct email subject and body.
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
    Sends the latest newsletter to all active subscribers, including a unique
    unsubscribe link for each recipient.

    The email is constructed using context information from the
    `new_newsletter` instance, a queryset of active subscribers, and predefined
    email templates.

    **Arguments:**
    - `new_newsletter`: An instance of :model:`support.Newsletter` containing
      the newsletter content.
    - `request`: The HTTP request used to build absolute URLs for links.

    **Context Data:**
    - `new_newsletter`: The newsletter instance.
    - `home_url`: Absolute URL to the home page.
    - `unsubscribe_url`: A unique absolute URL for each subscriber to
        unsubscribe.
    - `subscribers`: A queryset of active subscribers from
        :model:`support.Subscriber`.
    - `email`: The email address of each recipient.

    **Template:**
    :template:`staff/staff_emails/contact_reply_subject.txt`
    :template:`staff/staff_emails/contact_reply_body.html`
    """
    # Set variables for method.
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

        # Construct email subject and body.
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
    Renders the main staff dashboard, organized into tabs:

    - **Products and Realms**
    - **FAQs and FAQ Topics**
    - **Contact Messages**
    - **Newsletters and Subscribers**

    **Context Data:**
    - `faqs`: QuerySet of :model:`support.Faqs`
    - `faq_topics`: QuerySet of :model:`support.FaqsTopic`
    - `products`: QuerySet of :model:`products.Product`
    - `contact_messages`: QuerySet of :model:`support.ContactMessage`
    - `active_subscribers`: QuerySet of :model:`support.Subscriber`
    - `unconfirmed_subscribers`: QuerySet of :model:`support.Subscriber`
    - `expired_subscribers`: QuerySet of :model:`support.Subscriber`
    - `newsletters`: QuerySet of :model:`support.Newsletter`
    - `title`: String used to set the page's H1 title.
    - `active_tab`: The currently selected dashboard tab
        (defaults to 'Product' if not specified).

    **Template Used:**
    - :template:`staff/dashboard.html`

    **Returns:**
    - A rendered response containing the staff dashboard.
    """
    # Set variables for method.
    active_subscribers, unconfirmed_subscribers, expired_subscribers = (
        getSubscribers()
    )
    faqs = Faqs.objects.all()
    faq_topics = FaqsTopics.objects.all()
    products = Product.objects.all()
    contact_messages = ContactMessage.objects.all()
    newsletters = Newsletter.objects.all()

    active_tab = request.GET.get('tab')

    # Set view parameters
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

    # Set current tab to Product if one can't be found.
    if not context.get('active_tab'):
        context['active_tab'] = active_tab or 'Product'

    return render(request, template, context)


@staff_member_required
def manage_faq(request, delete=None, faq_id=None):
    """
    View to manage FAQs. Staff members can create, edit and delete instances
    of :model:`support.Faqs`

    **Arguments:**
    - `request`: The HTTP request.
    - `delete` (optional): Whether the request is to delete the specified Faqs
        instance.
    - `faq_id` (optional): The ID of an existing :model:`support.Faqs` to edit
        or delete.

    **Context:**
    - `active_tab`: set to 'FAQ' to dynamically set the dashboard tab.
    - `faqs`: Queryset of :model:`support.Faqs`
    - `mode`: Set to 'Delete', 'Update' or 'Add' for dynamically setting modal.
    - `return_url`: Set to return to the dashboard with the FAQs tab active.
    - `title`: String to dynamically set the H1 page heading.
    - `to_delete` (if mode is 'Delete'): Instance of :model:`support.Faqs`
    - `form` (if mode is not 'Delete'): Instance of :form:`support.FaqsForm`

    **Template:**
    - :template:`staff/dashboard.html`

    **Returns:**
    - **GET**: A rendered response to the dashboard page for FAQs
    - **POST**: Redirect back to the return_url with message if successful, if
        not a message is displayed.
    """
    # Set variables for the method.
    faqs = Faqs.objects.all()
    mode = 'Delete' if delete and faq_id else 'Update' if faq_id else 'Add'
    return_url = f"{reverse('dashboard')}?tab=FAQ"
    faq = None

    # Process request.
    if faq_id:
        faq = get_object_or_404(Faqs, pk=faq_id)

    if request.method == 'POST':
        if delete:
            try:
                faq.delete()
                messages.info(request, 'FAQ deleted')
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
                print('ERRORS FOUND: ', form.errors)
                messages.error(
                    request,
                    'Failed to update FAQ' if faq_id else 'Failed to add FAQ'
                )
    else:
        form = FaqsForm(instance=faq)

    # Set up view parameters
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
    View to manage FAQ topics. Staff members can create, edit and delete
    instances of :model:`support.FaqsTopics`

    **Arguments:**
    - `request`: The HTTP request.
    - `delete` (optional): Whether the request is to delete the specified Faqs
        Topics instance.
    - `faq_topic_id` (optional): The ID of an existing
        :model:`support.FaqsTopics` to edit or delete.

    **Context:**
    - `active_tab`: set to 'FAQ Topic' to dynamically set the dashboard tab.
    - `faq_topics`: Queryset of :model:`support.FaqsTopics`
    - `mode`: Set to 'Delete', 'Update' or 'Add' for dynamically setting modal.
    - `return_url`: Set to return to the dashboard with the FAQs tab active.
    - `associated`: Integer of how many instances of :model:`support.Faqs` have
        this topic as the ForeignKey.
    - `title`: String to dynamically set the H1 page heading.
    - `to_delete` (if mode is 'Delete'): Instance of
        :model:`support.FaqsTopics`
    - `form` (if mode is not 'Delete'): Instance of
        :form:`support.FaqsTopicsForm`

    **Template:**
    - :template:`staff/dashboard.html`

    **Returns:**
    - **GET**: A rendered response to the dashboard page for FAQs
    - **POST**: Redirect back to the return_url with message if successful, if
        not a message is displayed.
    """
    # Set variables for the method.
    faq_topics = FaqsTopics.objects.all()
    mode = (
        'Delete' if delete and faq_topic_id else
        'Update' if faq_topic_id else 'Add'
    )
    return_url = f"{reverse('dashboard')}?tab=FAQ"
    faq_topic = None

    # Process request.
    if faq_topic_id:
        faq_topic = get_object_or_404(FaqsTopics, pk=faq_topic_id)

    if request.method == 'POST':
        if delete:
            try:
                faq_topic.delete()
                messages.info(request, 'FAQ topic deleted')
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
    else:
        form = FaqsTopicsForm(instance=faq_topic)

    associated = faq_topic.faq_topic.count() if faq_topic else None

    # Set up view parameters
    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'FAQ Topic',
        'faq_topics': faq_topics,
        'mode': mode,
        'return_url': return_url,
        'associated': associated,
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
    View to manage products. Staff members can create, edit and delete
    instances of :model:`products.Product`

    **Arguments:**
    - `request`: The HTTP request.
    - `delete` (optional): Whether the request is to delete the specified
        Product instance.
    - `product_id` (optional): The ID of an existing
        :model:`products.Product` to edit or delete.

    **Context:**
    - `active_tab`: set to 'Product' to dynamically set the dashboard tab.
    - `products`: Queryset of :model:`products.Product`
    - `mode`: Set to 'Delete', 'Update' or 'Add' for dynamically setting modal.
    - `return_url`: Set to return to the dashboard with the Product tab active.
    - `title`: String to dynamically set the H1 page heading.
    - `to_delete` (if mode is 'Delete'): Instance of
        :model:`products.Product`
    - `form` (if mode is not `Delete`): Instance of
        :form:`products.ProductForm`

    **Template:**
    - :template:`staff/dashboard.html`

    **Returns:**
    - **GET**: A rendered response to the dashboard page for Products
    - **POST**: Redirect back to the return_url with message if successful, if
        not a message is displayed.
    """
    # Set variables for the method.
    products = Product.objects.all()
    mode = (
        'Delete' if delete and product_id else
        'Update' if product_id else 'Add'
    )
    return_url = f"{reverse('dashboard')}?tab=Product"
    product = None

    # Process request.
    if product_id:
        product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        if delete:
            try:
                product.delete()
                messages.info(request, 'Product deleted')
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

    # Set up view parameters
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
    View to manage Realms. Staff members can create, edit and delete
    instances of :model:`products.Realm`

    **Arguments:**
    - `request`: The HTTP request.
    - `delete` (optional): Whether the request is to delete the specified Realm
        instance.
    - `realm_id` (optional): The ID of an existing
        :model:`products.Realm` to edit or delete.

    **Context:**
    - `active_tab`: set to 'Product' to dynamically set the dashboard tab.
    - `products`: Queryset of :model:`products.Product`
    - `mode`: Set to 'Delete', 'Update' or 'Add' for dynamically setting modal.
    - `return_url`: Set to return to the dashboard with the Product tab active.
    - `associated`: Integer of how many instances of :model:`products.Product`
        have this realm as the ForeignKey.
    - `title`: String to dynamically set the H1 page heading.
    - `to_delete` (if mode is 'Delete'): Instance of
        :model:`products.Realm`
    - `form` (if mode is not 'Delete'): Instance of
        :form:`products.RealmForm`

    **Template:**
    - :template:`staff/dashboard.html`

    **Returns:**
    - **GET**: A rendered response to the dashboard page for Products
    - **POST**: Redirect back to the return_url with message if successful, if
        not a message is displayed.
    """
    # Set variables for the method.
    products = Product.objects.all()
    mode = (
        'Delete' if delete and realm_id else
        'Update' if realm_id else 'Add'
    )
    return_url = f"{reverse('dashboard')}?tab=Product"
    realm = None

    # Process request.
    if realm_id:
        realm = get_object_or_404(Realm, pk=realm_id)

    if request.method == 'POST':
        if delete:
            try:
                realm.delete()
                messages.info(request, 'Realm deleted')
                return redirect(return_url)
            except Exception as e:
                messages.error(request, f'Error deleting realm: {e}')
                return redirect(return_url)
        else:
            if realm_id:
                form = RealmForm(request.POST, instance=realm)
            else:
                new_realm_name = request.POST['name'].replace(' ', '_')
                prefix = request.POST.get('the_prefix_required')
                form = RealmForm({
                        'name': new_realm_name,
                        'the_prefix_required': prefix
                    })
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
        if realm:
            form = RealmForm(
                instance=realm, initial={'name': realm.display_name()}
            )
        else:
            form = RealmForm()

    associated = realm.product_realm.count() if realm else None

    # Set up view parameters
    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'Realm',
        'products': products,
        'mode': mode,
        'return_url': return_url,
        'associated': associated,
        'title': 'Staff Dashboard'
    }
    if mode == 'Delete':
        context['to_delete'] = realm
    else:
        context['form'] = form

    return render(request, template, context)


@staff_member_required
def manage_message(request, message_id, delete=None):
    """
    View to manage contact messages. Staff members can view, reply to
    and delete instances of :model:`support.ContactMessage` created via the
    contact us support page.

    **Arguments:**
    - `request`: The HTTP request.
    - `delete` (optional): Whether the request is to delete the specified
        message instance.
    - `message_id`: The ID of an existing :model:`support.ContactMessage` to
        reply to.

    **Context:**
    - `active_tab`: set to 'Message' to dynamically set the dashboard tab.
    - `contact_messages`: Queryset of :model:`support.ContactMessage`
    - `mode`: Set to 'Reply' for dynamically setting modal.
    - `return_url`: Set to return to the dashboard with the Message tab active.
    - `title`: String to dynamically set the H1 page heading.
    - `to_delete` (if mode is 'Delete'): Instance of
        :model:`support.ContactMessage`
    - `form` (if mode is not 'Delete'): Instance of
        :form:`support.ContactReplyForm`

    **Template:**
    - :template:`staff/dashboard.html`

    **Returns:**
    - **GET**: A rendered response to the dashboard page for Messages
    - **POST**: Redirect back to the return_url with message if successful, if
        not a message is displayed.
    """
    # Set variables for the method.
    contact_messages = ContactMessage.objects.all()
    mode = (
        'Delete' if delete and message_id else 'Reply'
    )
    return_url = f"{reverse('dashboard')}?tab=Message"
    message = get_object_or_404(ContactMessage, pk=message_id)

    # Process request.
    if request.method == 'POST':
        if delete:
            try:
                message.delete()
                messages.info(request, 'Message deleted')
                return redirect(return_url)
            except Exception as e:
                messages.error(request, f'Error deleting message: {e}')
                return redirect(return_url)
        else:
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

    # Set up view parameters
    template = 'staff/dashboard.html'
    context = {
        'active_tab': 'Message',
        'contact_messages': contact_messages,
        'mode': mode,
        'return_url': return_url,
        'title': 'Staff Dashboard'
    }
    if mode == 'Delete':
        context['to_delete'] = message
    else:
        context['form'] = form

    return render(request, template, context)


@staff_member_required
def manage_newsletters(request, delete=None, newsletter_id=None):
    """
    View to manage newsletters. Staff members can create and send new
    newsletters, as well as view and delete previous instances of
    :model:`support.Newsletter`.

    **Arguments:**
    - `request`: The HTTP request.
    - `delete` (optional): Whether the request is to delete the specified
        Newsletter instance.
    - `newsletter_id` (optional): The ID of an existing
        :model:`support.Newsletter` to view or delete.

    **Context:**
    - `active_tab`: set to 'Newsletter' to dynamically set the dashboard tab.
    - `active_subscribers`: Queryset of :model:`support.Subscriber`
    - `unconfirmed_subscribers`: Queryset of :model:`support.Subscriber`
    - `expired_subscribers`: Queryset of :model:`support.Subscriber`
    - `newsletters`: Queryset of :model:`support.Newsletter`
    - `mode`: Set to 'Delete', 'View' or 'Send' for dynamically setting modal.
    - `return_url`: Set to return to the dashboard with the Newsletter tab
        active.
    - `title`: String to dynamically set the H1 page heading.
    - `to_delete` (if mode is 'Delete'): Instance of
        :model:`support.Newsletter`
    - `form` (if mode is not 'Delete'): Instance of
        :form:`support.NewsletterForm`

    **Template:**
    - :template:`staff/dashboard.html`

    **Returns:**
    - **GET**: A rendered response to the dashboard page for Newsletter
    - **POST**: Redirect back to the return_url with message.
    """
    # Set variables for the method.
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

    # Process request.
    if newsletter_id:
        newsletter = get_object_or_404(Newsletter, pk=newsletter_id)

    if request.method == 'POST':
        if delete:
            try:
                newsletter.delete()
                messages.info(request, 'Newsletter deleted')
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
                return redirect(return_url)
            else:
                messages.error(
                    request,
                    'Failed to create newsletter, ensure form is valid')

    else:
        form = NewsletterForm(instance=newsletter)

    # Set up view parameters
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
    View to remove (unsubscribe) a subscriber from the mailing list by
    deleting the specified instance of :model:`support.Subscriber`.

    **Arguments:**
    - `request`: The HTTP request.
    - `subscriber_id`: The int ID of an existing :model:`support.Subscriber` to
        remove.

    **Context:**
    - `active_tab`: set to 'Newsletter' to dynamically set the dashboard tab.
    - `active_subscribers`: Queryset of :model:`support.Subscriber`
    - `unconfirmed_subscribers`: Queryset of :model:`support.Subscriber`
    - `expired_subscribers`: Queryset of :model:`support.Subscriber`
    - `newsletters`: Queryset of :model:`support.Newsletter`
    - `mode`: Set to 'Remove' for dynamically setting modal.
    - `return_url`: Set to return to the dashboard with the Newsletter tab
        active.
    - `to_delete`: Instance of :model:`support.Subscriber`
    - `title`: String to dynamically set the H1 page heading.

    **Template:**
    - :template:`staff/dashboard.html`

    **Returns:**
    - **GET**: A rendered response to the dashboard page for Newsletter
    - **POST**: Redirect back to the return_url with message.
    """
    # Set variables for the method.
    active_subscribers, unconfirmed_subscribers, expired_subscribers = (
        getSubscribers()
    )
    newsletters = Newsletter.objects.all()
    mode = 'Remove'
    return_url = f"{reverse('dashboard')}?tab=Newsletter"
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)

    # Process request.
    if request.method == 'POST':
        try:
            subscriber.delete()
            messages.success(request, 'Unsubscribed')
            return redirect(return_url)
        except Exception as e:
            messages.error(request, f'Error unsubscribing: {e}')
            return redirect(return_url)

    # Set up view parameters
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
    """
    View to remove all expired subscribers from the mailing list.

    **Arguments:**
    - `request`: The HTTP request.

    **Context:**
    - `active_tab`: set to 'Newsletter' to dynamically set the dashboard tab.
    - `active_subscribers`: Queryset of :model:`support.Subscriber`
    - `unconfirmed_subscribers`: Queryset of :model:`support.Subscriber`
    - `expired_subscribers`: Queryset of :model:`support.Subscriber`
    - `newsletters`: Queryset of :model:`support.Newsletter`
    - `mode`: Set to 'Clear' for dynamically setting modal.
    - `return_url`: Set to return to the dashboard with the Newsletter tab
        active.
    - `to_delete`: Queryset of :model:`support.Subscriber`
    - `title`: String to dynamically set the H1 page heading.

    **Template:**
    - :template:`staff/dashboard.html`

    **Returns:**
    - **GET**: A rendered response to the dashboard page for Newsletter
    - **POST**: Redirect back to the return_url with message.
    """
    # Set variables for the method.
    active_subscribers, unconfirmed_subscribers, expired_subscribers = (
        getSubscribers()
    )
    expired_subscribers = getSubscribers()[2]
    newsletters = Newsletter.objects.all()
    mode = 'Clear'
    return_url = f"{reverse('dashboard')}?tab=Newsletter"

    # Process request.
    if request.method == 'POST':
        if expired_subscribers.exists():
            expired_subscribers.delete()
            messages.success(request, 'All expired subscribers removed')
        else:
            messages.error(request, 'There are no expired subscribers')
        return redirect(return_url)

    # Set up view parameters
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


def cancel_action(request, action, tab, url):
    """
    View to inform user of cancelled actions. Message is compiled depending
    on the action the user was currently doing when they cancelled.

    **Arguments:**
    - `request`: The HTTP request.
    - `action`: The current mode that the view was in depending on what the
        user was doing. (Add, Update, Delete, View, Clear, Remove)
    - `tab`: The current dashboard tab the user is on.
    - `url`: The return url set from the view.

    **Returns:**
    - A redirect to the return url passed as url.
    """
    if 'FAQ' in tab:
        element = tab.lower().replace('faq', 'FAQ')
    else:
        element = tab.lower()

    # Compile the message.
    if action == 'Remove':
        message = 'Removing subscriber cancelled.'
    elif action == 'Clear':
        message = 'Clearing expired subscribers cancelled.'
    elif action == 'Reply':
        message = f'{action} to {element} cancelled.'
    else:
        message = f'{action} {element} cancelled.'

    # Send the message if the user wasn't in View mode.
    if action != 'View':
        messages.info(request, message)

    return redirect(url)
