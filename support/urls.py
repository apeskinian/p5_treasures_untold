from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('privacy/', views.privacy, name='privacy'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
