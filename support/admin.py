from django.contrib import admin
from .models import ContactMessage, Faqs, FaqsTopics


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'message', 'replied'
    )
    list_filter = ('replied',)


@admin.register(Faqs)
class FaqsAdmin(admin.ModelAdmin):
    list_display = (
        'topic', 'question', 'answer'
    )


admin.site.register(FaqsTopics)
