from django.contrib import admin
from django.core.management import call_command
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from products.models import Product


@admin.action(description='Recover abandoned baskets')
def recover_baskets(modeladmin, request, queryset):

    call_command('clear_abandoned_sessions')

    modeladmin.message_user(
        request,
        'Abandoned baskets have been recovered and sessions terminated.'
    )


@admin.action(description='Empty basket and recover stock')
def empty_basket(modeladmin, request, queryset):

    if 'basket' in request.session:
        basket = request.session.get('basket', {})

        for item_id, quantity in basket.items():
            try:
                product = get_object_or_404(Product, pk=item_id)
                updated_stock = product.stock
                updated_stock += quantity
                if updated_stock < 0:
                    raise ValueError('Stock cannot be negative.')
                elif product.unique_stock and updated_stock > 1:
                    raise ValueError(
                        'Stock cannot be more than one for unique items.'
                    )
                else:
                    product.stock += quantity
                    product.save()
            except ValueError:
                pass

        del request.session['basket']
        modeladmin.message_user(
            request,
            'Selected basket(s) have been cleared. Stock has been recovered.'
        )


@admin.action(description='Clear all currently activated rewards')
def clear_rewards(modeladmin, request, queryset):

    if 'rewards' in request.session:
        del request.session['rewards']
        modeladmin.message_user(
            request,
            'Reward data has been cleared for selected sessions.'
        )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    actions = [clear_rewards, recover_baskets, empty_basket]
