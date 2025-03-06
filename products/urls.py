from django.urls import path

from . import views

urlpatterns = [
    # View to show all products.
    path('', views.all_products, name='products'),

    # Shows a product in more detail with options to add to the basket.
    path('<int:product_id>/', views.product_detail, name='product_detail'),

    # View to activate or deactivate a reward with the standard arguments.
    path(
        'activate_reward/<str:action>/<str:reward>/',
        views.activate_reward,
        name='activate_reward'),

    # View to activate or deactivate rewards with an extra argument.
    path(
        'activate_reward/<str:action>/<str:reward>/<str:extra>',
        views.activate_reward,
        name='activate_reward')
]
