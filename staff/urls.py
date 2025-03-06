from django.urls import path

from . import views

urlpatterns = [
    # View to show the dashboard.
    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    # View to create a new FAQ.
    path(
        'manage_faq/',
        views.manage_faq,
        name='manage_faq'
    ),

    # View to edit a FAQ.
    path(
        'manage_faq/<int:faq_id>/',
        views.manage_faq,
        name='manage_faq'
    ),

    # View to delete a FAQ.
    path(
        'manage_faq/<str:delete>/<int:faq_id>/',
        views.manage_faq, name='manage_faq'
    ),

    # View to create a FAQ topic.
    path(
        'manage_faq_topic/',
        views.manage_faq_topic,
        name='manage_faq_topic'
    ),

    # View to edit a FAQ topic.
    path(
        'manage_faq_topic/<int:faq_topic_id>/',
        views.manage_faq_topic,
        name='manage_faq_topic'
    ),

    # View to delete a FAQ topic.
    path(
        'manage_faq_topic/<str:delete>/<int:faq_topic_id>/',
        views.manage_faq_topic,
        name='manage_faq_topic'
    ),

    # View to create a product.
    path('manage_product/',
         views.manage_product,
         name='manage_product'),

    # View to edit a product.
    path(
        'manage_product/<int:product_id>/',
        views.manage_product,
        name='manage_product'
    ),

    # View to delete a product.
    path(
        'manage_product/<str:delete>/<int:product_id>/',
        views.manage_product,
        name='manage_product'
    ),

    # View to create a realm.
    path('manage_realm/',
         views.manage_realm,
         name='manage_realm'),

    # View to edit a realm.
    path(
        'manage_realm/<int:realm_id>/',
        views.manage_realm,
        name='manage_realm'
    ),

    # View to delete a realm.
    path(
        'manage_realm/<str:delete>/<int:realm_id>/',
        views.manage_realm,
        name='manage_realm'
    ),

    # View to reply to a message.
    path(
        'reply_to_message/<int:message_id>/',
        views.reply_to_message,
        name='reply_to_message'
    ),

    # View to remove a specific subscriber.
    path(
        'manage_subscriber/<int:subscriber_id>/',
        views.manage_subscriber,
        name='manage_subscriber'
    ),

    # View to remove all expired subscribers.
    path(
        'clear_expired/',
        views.clear_expired_subscribers,
        name='clear_expired_subscribers'
    ),

    # View to create a newsletter and send it.
    path(
        'manage_newsletters/',
        views.manage_newsletters,
        name='manage_newsletters'
    ),

    # View to see a previous newsletter.
    path(
        'manage_newsletters/<int:newsletter_id>/',
        views.manage_newsletters,
        name='manage_newsletters'
    ),

    # View to delete a previous newsletter.
    path(
        'manage_newsletters/<str:delete>/<int:newsletter_id>/',
        views.manage_newsletters,
        name='manage_newsletters'
    ),
]
