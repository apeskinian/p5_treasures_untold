from django.contrib import admin
from .models import Realm, Product

# registering models
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
    list_filter = ('realm',)
    ordering = ('realm__name', 'name')