from django.contrib import admin
from .models import Realm, Product

# registering models
admin.site.register(Realm)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'realm', 'sku', 'price', 'stock')
    list_filter = ('realm',)