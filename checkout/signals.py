from django.db.models.signals import post_save, post_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings
from .models import OrderLineItem


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
