from django.shortcuts import render


def faq(request):
    """
    a view to show the faqs for the site
    """
    template = 'support/support.html'
    context = {
        'title': 'FAQs'
    }

    return render(request, template, context)


def contact(request):
    """
    a view to show the contact page for the site
    """
    template = 'support/support.html'
    context = {
        'title': 'Contact Us'
    }

    return render(request, template, context)


def newsletter(request):
    """
    a view to show the newsletter for the site
    """
    template = 'support/support.html'
    context = {
        'title': 'Newsletter'
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
