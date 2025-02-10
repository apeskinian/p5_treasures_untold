from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('privacy/', views.privacy, name='privacy'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('faq_admin/', views.faq_admin, name='faq_admin'),
    path('add_faq/', views.add_faq, name='add_faq'),
    path('edit_faq/<int:faq_id>', views.edit_faq, name='edit_faq'),
    path('delete_faq/<int:faq_id>', views.delete_faq, name='delete_faq'),
]
