from django.contrib import admin
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404

from products.models import Product


@admin.action(description='Empty basket and recover stock')
def empty_basket(modeladmin, request, queryset):
    """
    Empty the basket of the selected session and recover any items that are
    currently in the basket.
    """
    for session in queryset:
        session_data = session.get_decoded()
        if 'basket' in session_data:
            basket = session_data.get('basket', {})

            # Iterate through basket and restock for each item.
            for item_id, quantity in basket.items():
                try:
                    product = get_object_or_404(Product, pk=item_id)
                    updated_stock = product.stock
                    updated_stock += quantity
                    if updated_stock < 0:
                        product.stock = 0
                        product.save()
                        raise ValueError('Stock cannot be negative.')
                    elif product.unique_stock and updated_stock > 1:
                        product.stock = 1
                        product.save()
                        raise ValueError(
                            'Stock cannot be more than one for unique items.'
                        )
                    else:
                        product.stock += quantity
                        product.save()
                except ValueError:
                    pass

            # Delete the basket from the session and save.
            del session_data['basket']
            store = SessionStore(session_key=session.session_key)
            store.modified = True
            store.clear()
            store.update(session_data)
            store.save()

        if request.session.session_key == session.session_key:
            if 'basket' in request.session:
                del request.session['basket']

    modeladmin.message_user(
        request,
        'Selected basket(s) have been cleared. Stock has been recovered.'
    )


@admin.action(description='Deactivate rewards')
def clear_rewards(modeladmin, request, queryset):
    """
    Clears any currently activated rewards in the selected session.
    """
    for session in queryset:
        session_data = session.get_decoded()
        if 'rewards' in session_data:
            del session_data['rewards']
            store = SessionStore(session_key=session.session_key)
            store.modified = True
            store.clear()
            store.update(session_data)
            store.save()

        if request.session.session_key == session.session_key:
            if 'rewards' in request.session:
                del request.session['rewards']

    modeladmin.message_user(
        request,
        'Reward data has been cleared for selected sessions.'
    )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    actions = [clear_rewards, empty_basket]
