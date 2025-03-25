from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST

from itsdangerous import URLSafeTimedSerializer

from .forms import ContactForm, SubscriberForm
from .models import Faqs, FaqsTopics, Subscriber


def generate_confirmation_token(subscriber):
    """
    Generates a time-sensitive token for newsletter signup confirmation.

    Uses `itsdangerous.URLSafeTimedSerializer` to create a signed token
    based on the subscriber's email. This token can later be used to verify
    the signup request.

    **Arguments:**
    - subscriber (:model:`support.Subscriber`): The subscriber instance.

    **Returns:**
    - str: A signed token for email confirmation.
    """
    serializer = URLSafeTimedSerializer(settings.DANGEROUS_SECRET)
    return serializer.dumps(subscriber.email, salt='email-confirmation')


def sendSubscriptionConfirmationEmail(email, confirmation_url, request):
    """
    Sends a confirmation email after a user subscribes to the newsletter.

    The email contains a unique `confirmation_url`, generated using an
    `itsdangerous` token, allowing the user to confirm their subscription.

    The email is constructed using `email` and `confirmation_url` that is
    passed and the email templates.

    **Arguments:**
    - `email`: The email address of the subscriber.
    - `confirmation_url`: A unique URL generated with an `itsdangerous` token.
    - `request`: The HTTP request used to generate an absolute url.

    **Context:**
    - `home_url`: Absolute URL to the home page.
    - `confirmation_url`: The generated confirmation link.
    - `email`: The email address of the subscriber.

    **Template:**
    :template:`support/support_emails/subscription_confirmation_subject.txt`
    :template:`support/support_emails/subscription_confirmation_body.html`
    """
    # Set variables for method.
    home_url = request.build_absolute_uri(reverse('home'))

    # Construct email subject and body.
    subject = render_to_string(
        'support/support_emails/subscription_confirmation_subject.txt'
    )
    html_message = render_to_string(
        'support/support_emails/subscription_confirmation_body.html',
        {
            'confirmation_url': confirmation_url,
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


def sendMessageAcknowledgementEmail(name, email, request, ticket_number):
    """
    Sends an acknowledgment email after a user submits a contact form.
    The email informs the user that their message has been received and
    provides a unique `ticket_number` for reference.

    The email is constructed using the context information and the templates.

    **Arguments:**
    - `name`: The name of the recipient.
    - `email`: The email address of the recipient.
    - `ticket_number`: A unique ticket number generated when the the message
        was created.
    - `request`: The HTTP request used to generate absolute urls.

    **Context:**
    - `products_url`: Absolute URL to the products page.
    - `home_url`: Absolute URL to the home page.
    - `ticket_number`: The generated ticket number.
    - `email`: The email address of the recipient.

    **Template:**
    :template:`support/support_emails/contact_acknowledgment_subject.txt`
    :template:`support/support_emails/contact_acknowledgment_body.html`
    """
    # Set variables for method.
    products_url = request.build_absolute_uri(reverse('products'))
    home_url = request.build_absolute_uri(reverse('home'))

    # Construct email subject and body.
    subject = render_to_string(
        'support/support_emails/contact_acknowledgment_subject.txt',
        {'ticket_number': ticket_number}
    )
    html_message = render_to_string(
        'support/support_emails/contact_acknowledgment_body.html',
        {
            'name': name,
            'products_url': products_url,
            'home_url': home_url,
            'ticket_number': ticket_number
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


def faq(request):
    """
    Displays the Frequently Asked Questions (FAQs) page.

    **Context:**
    - `title`: Used to dynamically set the H1 page heading.
    - `content`: Used to dynamically load the correct includes file in the
        template.
    - `faqs_list`: Queryset of :model:`support.Faqs`
    - `topics`: Queryset of :model:`support.FaqsTopics`

    **Template:**
    - :template:`support/support.html`

    **Returns:**
    - A render response to show the FAQs page.
    """
    # Set up variables for method.
    faqs_list = Faqs.objects.all().order_by('topic')
    topics = FaqsTopics.objects.all()

    # Set up view parameters.
    template = 'support/support.html'
    context = {
        'title': 'FAQs',
        'content': 'faq',
        'faqs_list': faqs_list,
        'topics': topics
    }

    return render(request, template, context)


def contact(request):
    """
    Displays the contact us page for the site where users can submit a
    message including their name and email for a reply.

    Upon successful form submission the `sendMessageAcknowledgementEmail`
    method is called to send them an email.

    **Context:**
    - `title`: Used to dynamically set the H1 page heading.
    - `content`: Used to dynamically load the correct includes file in the
        template.
    - `form`: Instance of :form:`support.ContactForm`

    **Template:**
    - :template:`support/contact.html`

    **Returns:**
    - **GET**: A render response to the show the contact us page.
    - **POST**: On successful form submission a redirect to `thankyou`
        otherwise an error message to check form validation.
    """
    # Handle form submission.
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message']
        }
        contact_form = ContactForm(form_data)
        if contact_form.is_valid():
            contact_message = contact_form.save()
            ticket_number = contact_message.ticket_number
            messages.success(
                request,
                'Message received, thank you.'
            )
            sendMessageAcknowledgementEmail(
                form_data['name'],
                form_data['email'],
                request,
                ticket_number=ticket_number,
            )
            return redirect(reverse('thankyou'))
        else:
            messages.error(
                request,
                'There was a problem sending your message,'
                'please ensure the form is valid'
            )
    else:
        # Initiate form.
        contact_form = ContactForm()

    # Set up view parameters.
    template = 'support/support.html'
    context = {
        'title': 'Contact Us',
        'content': 'contact',
        'form': contact_form
    }

    return render(request, template, context)


def thankyou(request):
    """
    Displays a thank you message when a user successfully sends a message
    from the contact us page.

    **Context:**
    - `title`: Used to dynamically set the H1 page heading.
    - `content`: Used to dynamically load the correct includes file in the
        template.

    **Returns:**
    - A render response to show the thank you page.
    """
    # Set up view parameters
    template = 'support/support.html'
    context = {
        'title': 'Thank You',
        'content': 'thankyou'
    }

    return render(request, template, context)


def newsletter(request):
    """
    Displays the newsletter information page where a user can sign up to
    reieve the letter via email.

    **Context:**
    - `title`: Used to dynamically set the H1 page heading.
    - `content`: Used to dynamically load the correct includes file in the
        template.
    - `main_subscriber_form`: Instance of :form:`support.SubscriberForm`
        prefixed with 'main_newsletter' to avoid interference with the other
        newsletter sign-up form in the `info_section.html` included at the
        bottom of the template.

    **Returns:**
    - A render response to show the newsletter page.
    """
    # Set variables for method.
    main_subscriber_form = SubscriberForm(prefix='main_newsletter')

    # Set view parameters.
    template = 'support/support.html'
    context = {
        'title': 'Newsletter',
        'content': 'newsletter',
        'main_subscriber_form': main_subscriber_form
    }

    return render(request, template, context)


@require_POST
def subscribe(request):
    """
    Handles subscription requests to the newsletter, which can come from
    any page with the `info_section.html` includes file or the main
    newsletter support page.

    **Process:**
    - On successful form submission, the email is checked against the
        subscriber model to determine if the email exists and whether it
        has been confirmed.
    - If the email already exists and is confirmed, the user is shown
        a message: 'This email has already been subscribed'.
    - If the email does not exist or is not confirmed, a confirmation URL
        is generated and sent via email to the user.
    - After processing, the user is redirected to the `HTTP_REFERER` page.

    **Returns:**
    - A redirect to the page the user came from, using the `HTTP_REFERER`
        header.
    """
    # Set variables for method.
    return_url = request.META.get('HTTP_REFERER')
    form_email = (
        request.POST.get('newsletter-email') or
        request.POST.get('main_newsletter-email')
    )
    subscribe_form = SubscriberForm({'email': form_email})

    # Handle form submission.
    if subscribe_form.is_valid():

        email = subscribe_form.cleaned_data['email']
        subscriber, created = Subscriber.objects.get_or_create(email=email)

        # Check for email already in db of subscribers.
        if not created and subscriber.is_active:
            messages.info(request, 'This email has already been subscribed')
            return redirect(return_url)

        token = generate_confirmation_token(subscriber)

        confirmation_url = (
            request.build_absolute_uri(reverse('confirm_subscription',
                                               args=[subscriber.id, token]))
        )

        subscriber.token = token
        subscriber.token_created_at = timezone.now()
        subscriber.save()

        # Send email to confirm subscription.
        sendSubscriptionConfirmationEmail(email, confirmation_url, request)
        messages.success(
            request,
            'Thank you for subscribing! You will receive an email with a link '
            'to confirm the subscription'
        )
    else:
        for errors in subscribe_form.errors.values():
            for error in errors:
                messages.error(request, error)
        return redirect(return_url)

    return redirect(return_url)


def confirm_subscription(request, subscriber_id, token):
    """
    Handles the subscription confirmation process when a subscriber
    clicks on the link in the email sent to them.

    **Process:**
    - The `token_created_at` timestamp is compared to the `token_expiry`
      limit (set to 1 day).
    - If the token has expired or is invalid, the user is shown the message:
      'Your confirmation link has expired, please try again.' and redirected
      to the newsletter page.
    - If the token is valid and within the expiry time, the subscriber's
      status is updated to active, and they are redirected to a success page.

    **Context:**
    - `title`: Used to dynamically set the H1 page heading.
    - `content`: Used to dynamically load the correct includes file in the
        template.

    **Template:**
    - :template:`support/support.html`

    **Returns:**
    - A render response to the success page on successful confirmation.
    - A redirect to the newsletter page for all other results.
    """
    # Set variables for method.
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)

    # Validate token and process.
    if subscriber.token == token:

        token_expiry = timedelta(days=1)
        if subscriber.token_created_at < timezone.now() - token_expiry:
            subscriber.delete()
            messages.error(
                request,
                'Your confirmation link has expired, please try again.'
            )
            return redirect(reverse('newsletter'))

        subscriber.date_joined = timezone.localdate()
        subscriber.is_active = True
        subscriber.save()

        # Set view parameters.
        template = 'support/support.html'
        context = {
            'title': 'Success',
            'content': 'newsletter_success',
        }

        return render(request, template, context)
    else:
        messages.error(
            request,
            'Invalid token - please try again. If this problem persists please'
            ' contact us'
            )
        return redirect(reverse('newsletter'))


def confirm_unsubscription(request, subscriber_id, token):
    """
    Handles the unsubscription process when a user clicks on the unique
    unsubscribe link in the newsletter.

    **Process:**
    - If the provided token is valid, the subscriber is unsubscribed,
        and the message 'You have been unsubscribed' is shown.
    - If the token is invalid, the message 'There was an error, please
        contact admin' is shown.

    **Returns:**
    - A redirect to the home page (`home`) after either unsubscription or
        error.
    """
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)
    if subscriber.token == token:
        subscriber.delete()
        messages.info(request, 'You have been unsubscribed')
        return redirect(reverse('home'))
    else:
        messages.error(request, 'The was an error please contact admin')
        return redirect(reverse('home'))


def privacy(request):
    """
    Displays the privacy policy.

    **Context:**
    - `title`: Used to dynamically set the H1 page heading.
    - `content`: Used to dynamically load the correct includes file in the
        template.

    **Template:**
    - :template:`support/support.html`

    **Returns:**
    - A render response to show the privacy policy page.
    """
    # Set view parameters
    template = 'support/support.html'
    context = {
        'title': 'Privacy Statement',
        'content': 'privacy'
    }

    return render(request, template, context)


def returns(request):
    """
    Displays the returns policy.

    **Context:**
    - `title`: Used to dynamically set the H1 page heading.
    - `content`: Used to dynamically load the correct includes file in the
        template.

    **Template:**
    - :template:`support/support.html`

    **Returns:**
    - A render response to show the returns policy page.
    """
    # Set view parameters
    template = 'support/support.html'
    context = {
        'title': 'Returns Policy',
        'content': 'returns'
    }

    return render(request, template, context)


def terms(request):
    """
    Displays the terms and conditions.

    **Context:**
    - `title`: Used to dynamically set the H1 page heading.
    - `content`: Used to dynamically load the correct includes file in the
        template.

    **Template:**
    - :template:`support/support.html`

    **Returns:**
    - A render response to show the terms and conditions page.
    """
    # Set view parameters
    template = 'support/support.html'
    context = {
        'title': 'Terms and Conditions',
        'content': 'terms'
    }

    return render(request, template, context)
