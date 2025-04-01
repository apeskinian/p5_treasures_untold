from django.contrib import admin

from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp

from .models import ContactMessage, Faqs, FaqsTopics, Newsletter, Subscriber


admin.site.register(FaqsTopics)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'ticket_number', 'name', 'email', 'message', 'replied'
    )
    list_filter = ('replied',)
    readonly_fields = ('reply',)


@admin.register(Faqs)
class FaqsAdmin(admin.ModelAdmin):
    list_display = (
        'topic', 'question', 'answer'
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'subject', 'date_sent'
    )
    ordering = ['-date_sent']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'date_joined'
    )
    ordering = ['-date_joined']


admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
