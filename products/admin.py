from django.contrib import admin
from django.db.models.functions import Lower

from .models import Realm, Product


@admin.register(Realm)
class RealmAdmin(admin.ModelAdmin):
    list_display = ('display_name',)
    ordering = (Lower('name'),)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'realm_name', 'sku', 'price',
        'stock', 'unique_stock', 'date_added'
    )
    list_editable = ('stock', 'unique_stock',)
    list_filter = ('realm',)
    ordering = (Lower('realm__name'), 'name')

    @admin.action(description='Restock items')
    def restock(self, request, queryset):
        """
        Restocks selected item makes stock level 50 unless the item is unique
        and then sets it to 1
        """
        for product in queryset:
            if product.unique_stock:
                product.stock = 1
            else:
                product.stock = 50
            product.save()

    actions = [restock]
