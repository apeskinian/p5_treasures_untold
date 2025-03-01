from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request, order_number=None):
    """
    a view to show the user profile and order history
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    view_order = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid'
            )
    else:
        form = UserProfileForm(instance=profile)

    if order_number:
        view_order = get_object_or_404(Order, order_number=order_number)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        'view_order': view_order if view_order else None
    }

    return render(request, template, context)
