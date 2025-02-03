from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'order_total',
        'discount',
        'delivery_cost',
        'grand_total',
    )
    fields = (
        'order_number',
        'date',
        'full_name',
        'phone_number',
        'street_address_1',
        'street_address_2',
        'town_city',
        'county',
        'postcode',
        'country',
        'order_total',
        'discount',
        'delivery_cost',
        'grand_total',
    )
    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'discount',
        'delivery_cost',
        'grand_total',
    )
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
