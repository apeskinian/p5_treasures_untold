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

from .models import Faqs, FaqsTopics, Subscriber
from .forms import ContactForm, SubscriberForm


def generate_confirmation_token(subscriber):
    """
    Generate a token for newsletter signup confirmation.
    """
    serializer = URLSafeTimedSerializer(settings.DANGEROUS_SECRET)
    return serializer.dumps(subscriber.email, salt='email-confirmation')


def sendMessageAcknowledgementEmail(name, email, request, ticket_number):
    """
    Send the user an email to confirm receipt of their message.
    """
    products_url = request.build_absolute_uri(reverse('products'))
    home_url = request.build_absolute_uri(reverse('home'))
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
    A view to show the faqs for the site.
    """
    faqs_list = Faqs.objects.all().order_by('topic')
    topics = FaqsTopics.objects.all()

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
    A view to show the contact page for the site.
    """
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
        contact_form = ContactForm()

    template = 'support/support.html'
    context = {
        'title': 'Contact Us',
        'content': 'contact',
        'form': contact_form
    }

    return render(request, template, context)


def thankyou(request):
    """
    A confirmation page for when a user sends a message via the contact form.
    """
    template = 'support/support.html'
    context = {
        'title': 'Thank You',
        'content': 'thankyou'
    }

    return render(request, template, context)


def newsletter(request):
    """
    A view to show the newsletter for the site.
    """
    main_subscriber_form = SubscriberForm()

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
    Checks to see if a user is already subscribed and then if not:
    - creates a subscriber instance and generates a token
    - sends the subscriber an email for them to confirm
    """
    return_url = request.META.get('HTTP_REFERER')
    subscribe_form = SubscriberForm(request.POST)

    if subscribe_form.is_valid():
        email = subscribe_form.cleaned_data['email']
        subscriber, created = Subscriber.objects.get_or_create(email=email)

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

        send_mail(
            'Confirm your subscription',
            f'Click here to confirm your subscription: {confirmation_url}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
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
    Handles the confirmation request when a subscriber clicks on the
    link in the email that was sent to them. If the link was clicked
    before the expiration:
    - the subscriber is marked as active
    - they are directed to the success page
    """
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)

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
    Handles requests from subscribers to unsubscribe. This will be from a
    link in emails that are sent to them in the newsletter.
    """
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)
    if subscriber.token == token:
        subscriber.delete()
        messages.error(request, 'Have been unsubscribed')
        return redirect(reverse('home'))
    else:
        messages.error(request, 'The was an error please contact admin')
        return redirect(reverse('home'))


def privacy(request):
    """
    A view to show the privacy statement for the site.
    """
    template = 'support/support.html'
    context = {
        'title': 'Privacy Statement',
        'content': 'privacy'
    }

    return render(request, template, context)
