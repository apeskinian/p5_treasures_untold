from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from checkout.models import Order
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request, order_number=None):
    """
    A view to show the user's profile and order history. If an `order_number`
    is provided, it will also show the selected order in a modal.

    **Arguments:**
    - `request`: The HTTP request.
    - `order_number`: Optional. Used to get the instance of
        :model:`checkout.Order` to show as context for a specific order.

    **Context:**
    - `form`: Instance of :form:`profiles.UserProfileForm` prefilled with any
        saved details for the user.
    - `orders`: Queryset of :model:`checkout.Order` belonging to the user,
        sorted by date (latest first).
    - `profile`: An instance of :model:`profiles.UserProfile` for the current
        user.
    - `view_order`: If an `order_number` is provided, this will be an instance
        of :model:`checkout.Order` for the specified order.

    **Template:**
    - `profiles/profile.html`

    **Returns:**
    - A render response with the context and `view_order` if an `order_number`
        is specified, or an empty context otherwise.
    """
    # Set variables for method.
    profile = get_object_or_404(UserProfile, user=request.user)
    view_order = None

    # Update user details on form submission.
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

    # Retrieve previous order details if requested.
    if order_number:
        view_order = get_object_or_404(Order, order_number=order_number)

    orders = profile.orders.all().order_by('-date')

    # Set up view parameters.
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        'view_order': view_order if view_order else None
    }

    return render(request, template, context)
