from django.contrib.auth.signals import user_logged_out
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from products.models import Product

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Calls the `update_total` method on the related order when an OrderLineItem
    is saved (created or updated).

    **Arguments:**
    - `sender`: The model class that sent the signal.
    - `instance`: The instance of the OrderLineItem that was saved.
    - `created`: Boolean indicating if the instance was created or updated.
    - `kwargs`: Additional keyword arguments passed with the signal.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Calls the `update_total` method on the related order when an OrderLineItem
    is deleted.

    **Arguments:**
    - `sender`: The model class that sent the signal.
    - `instance`: The instance of the OrderLineItem that was deleted.
    - `kwargs`: Additional keyword arguments passed with the signal.
    """
    instance.order.update_total()


@receiver(user_logged_out)
def clear_session_on_logout(sender, request, user, **kwargs):
    """
    Clears the session's basket and reward data when the user logs out.
    It also recovers any items left in the basket and updates stock levels
    accordingly.

    **Arguments:**
    - `sender`: The sender of the signal, which is the user logged out event.
    - `request`: The HTTP request object.
    - `user`: The user who logged out.
    - `kwargs`: Additional keyword arguments passed with the signal.
    """
    # Check for items left in basket session data.
    if 'basket' in request.session:
        basket = request.session.get('basket', {})

        for item_id, quantity in basket.items():
            try:
                product = get_object_or_404(Product, pk=item_id)
                updated_stock = product.stock
                updated_stock += quantity
                if updated_stock < 0:
                    product.stock = 0
                    product.save()
                    raise ValueError('Stock cannot be negative.')
                elif product.unique_stock and updated_stock > 1:
                    product.stock = 1
                    product.save()
                    raise ValueError(
                        'Stock cannot be more than one for unique items'
                    )
                else:
                    product.stock += quantity
                    product.save()
            except ValueError:
                pass

        del request.session['basket']

    # Check for rewards in session data.
    if 'rewards' in request.session:
        del request.session['rewards']
