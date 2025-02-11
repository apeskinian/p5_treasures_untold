from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('manage_faq/', views.manage_faq, name='manage_faq'),
    path('manage_faq/<int:faq_id>/', views.manage_faq, name='manage_faq'),
    # path('manage_faq/<str:delete>/<int:faq_id>/', views.manage_faq, name='manage_faq'),
    path('delete_faq/<int:faq_id>/', views.delete_faq, name='delete_faq'),
]
