from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('privacy/', views.privacy, name='privacy'),
]
