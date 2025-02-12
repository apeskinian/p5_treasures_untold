from django.views.decorators.http import require_POST
from django.shortcuts import render, reverse, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Faqs, FaqsTopics
from .forms import ContactForm, NewsletterForm
from django.contrib import messages


def sendMessageAcknowledgementEmail(name, email, request, ticket_number):
    """
    send the user an email to confirm receipt of their message
    """
    products_url = request.build_absolute_uri(reverse('products'))
    home_url = request.build_absolute_uri(reverse('home'))
    subject = render_to_string(
        'support/contact_emails/contact_acknowledgment_subject.txt',
        {'ticket_number': ticket_number}
    )
    html_message = render_to_string(
        'support/contact_emails/contact_acknowledgment_body.html',
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
    a view to show the faqs for the site
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
    a view to show the contact page for the site
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
    a confirmation page for when a user sends a message via the contact form
    """
    template = 'support/support.html'
    context = {
        'title': 'Thank You',
        'content': 'thankyou'
    }

    return render(request, template, context)


def newsletter(request):
    """
    a view to show the newsletter for the site
    """
    main_newsletter_form = NewsletterForm()

    template = 'support/support.html'
    context = {
        'title': 'Newsletter',
        'content': 'newsletter',
        'main_newsletter_form': main_newsletter_form
    }

    return render(request, template, context)


@require_POST
def subscribe(request):
    """
    Signs the user up to the newsletter
    """
    return_url = request.META.get('HTTP_REFERER')
    news_form = NewsletterForm(request.POST)
    if news_form.is_valid():
        news_form.save()
        messages.success(request, 'Thank you for subscribing!')
    else:
        for errors in news_form.errors.values():
            for error in errors:
                messages.error(request, error)
        return redirect(return_url)

    template = 'support/support.html'
    context = {
        'title': 'Success',
        'content': 'newsletter_success',
        'return_url': return_url
    }

    return render(request, template, context)


def privacy(request):
    """
    a view to show the privacy statement for the site
    """
    template = 'support/support.html'
    context = {
        'title': 'Privacy Statement',
        'content': 'privacy'
    }

    return render(request, template, context)
