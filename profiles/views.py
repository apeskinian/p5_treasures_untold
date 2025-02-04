from django.shortcuts import render


def profile(request):
    """
    a view to show the user profile and order history
    """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
