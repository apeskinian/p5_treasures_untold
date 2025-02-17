from django.db.models.signals import post_save, post_delete
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from .models import OrderLineItem
from products.models import Product
from django.shortcuts import get_object_or_404


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    update order total on lineitem delete
    """
    instance.order.update_total()


@receiver(user_logged_out)
def clear_session_on_logout(sender, request, user, **kwargs):
    """
    clears user session data on user logged out event
    """
    if 'basket' in request.session:
        basket = request.session.get('basket', {})

        for item_id, quantity in basket.items():
            try:
                product = get_object_or_404(Product, pk=item_id)
                updated_stock = product.stock
                updated_stock += quantity
                if updated_stock < 0:
                    raise ValueError('Stock cannot be negative.')
                elif product.unique_stock and updated_stock > 1:
                    raise ValueError(
                        'Stock cannot be more than one for unique items'
                    )
                else:
                    product.stock += quantity
                    product.save()
            except ValueError:
                pass

        del request.session['basket']
    if 'rewards' in request.session:
        del request.session['rewards']
