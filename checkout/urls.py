from django.urls import path

from . import views
from .webhooks import webhook


urlpatterns = [
    # View for completing purchse and processing payment.
    path('', views.checkout, name='checkout'),

    # Confirmation view of transaction.
    path(
        'checkout_success/<order_number>',
        views.checkout_success,
        name='checkout_success'
    ),

    # Adding extra data to payment intent metadata.
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
    ),

    # Webhook handler
    path('wh/', webhook, name='webhook')
]
