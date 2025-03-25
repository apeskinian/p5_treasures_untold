from django.urls import path
from . import views

urlpatterns = [
     # View to the FAQs page.
     path('faq/', views.faq, name='faq'),

     # View to the contact us page.
     path('contact/', views.contact, name='contact'),

     # View to the newsletter page.
     path('newsletter/', views.newsletter, name='newsletter'),

     # View to the subscribe page.
     path('subscribe/', views.subscribe, name='subscribe'),

     # View to the privacy policy page.
     path('privacy/', views.privacy, name='privacy'),

     # View to the return policy page.
     path('returns/', views.returns, name='returns'),

     # View to the terms and conditions page.
     path('terms/', views.terms, name='terms'),

     # View to the subscription confirmation page.
     path('confirm/<int:subscriber_id>/<token>/',
          views.confirm_subscription,
          name='confirm_subscription'
          ),

     # View to the unsubscribe confirmation which send the user to the home
     # page with a message.
     path('unsubscribe/<int:subscriber_id>/<token>/',
          views.confirm_unsubscription,
          name='confirm_unsubscription'
          ),
]
