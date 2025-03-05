from django.urls import path
from . import views

urlpatterns = [
    # View the contents of the basket.
    path('', views.view_basket, name='view_basket'),

    # Add an item to the basket using item_id as an argument.
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),

    # Adjust an item in the basket using item_id as an argument.
    path('adjust/<item_id>/', views.adjust_basket, name='adjust_basket'),

    # Remove an item from the basket using item_id as an argument.
    path(
        'remove/<item_id>/',
        views.remove_from_basket,
        name='remove_from_basket'
    ),
]
