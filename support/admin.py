from django.contrib import admin
from .models import contactMessage


@admin.register(contactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'message', 'replied'
    )
    list_filter = ('replied',)
