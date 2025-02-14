from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path(
        'activate_reward/',
        views.activate_reward,
        name='activate_reward'),
    path(
        'activate_reward/<str:reward>',
        views.activate_reward,
        name='activate_reward'),
]
