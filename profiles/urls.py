from django.urls import path

from . import views


urlpatterns = [
    # View to show the user profile.
    path('', views.profile, name='profile'),

    # View a previous order.
    path(
        'order_history/<order_number>',
        views.profile,
        name='order_history'
    ),
]
