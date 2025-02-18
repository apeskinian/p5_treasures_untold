from django.contrib import admin
from .models import Realm, Product


@admin.register(Realm)
class RealmAdmin(admin.ModelAdmin):
    list_display = ('display_name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'realm_name', 'sku', 'price',
        'stock', 'unique_stock', 'date_added'
    )
    list_editable = ('stock', 'unique_stock',)
    list_filter = ('realm',)
    ordering = ('realm__name', 'name')
