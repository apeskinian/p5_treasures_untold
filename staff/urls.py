from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('manage_faq/', views.manage_faq, name='manage_faq'),
    path('manage_faq/<int:faq_id>/', views.manage_faq, name='manage_faq'),
    path(
        'manage_faq/<str:delete>/<int:faq_id>/',
        views.manage_faq, name='manage_faq'
    ),
    path('manage_product/', views.manage_product, name='manage_product'),
    path(
        'manage_product/<int:product_id>/',
        views.manage_product,
        name='manage_product'
    ),
    path(
        'manage_product/<str:delete>/<int:product_id>/',
        views.manage_product, name='manage_product'
    ),
    path(
        'reply_to_message/<int:message_id>/',
        views.reply_to_message, name='reply_to_message'
    ),
]
