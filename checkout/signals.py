from django.db.models.signals import post_save, post_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings
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


@receiver(user_logged_in)
def reset_discount_on_login(sender, request, user, **kwargs):
    """
    reset discount to 0 on user logged in event
    """
    settings.DISCOUNT = 0


@receiver(user_logged_out)
def reset_discount_on_logout(sender, request, user, **kwargs):
    """
    reset discount to 0 on user logged out event
    """
    settings.DISCOUNT = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        product.stock += quantity
        if product.stock < 0:
            raise ValueError('Stock cannot be negative.')
        product.save()

    request.session['basket'] = {}
    request.session['rewards'] = []
    request.session.modified = True
