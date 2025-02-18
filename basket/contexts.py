from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = settings.DELIVERY
    basket = request.session.get('basket', {})
    rewards = request.session.get('rewards', [])
    original_total = 0

    for index, (item_id, quantity) in enumerate(basket.items()):
        product = get_object_or_404(Product, pk=item_id)
        if index < 3 and 'magic-lamp' in rewards:
            original_price = product.price
            product.price = 0
        if product.realm.name == 'Agrabah' and 'cave-of-wonders' in rewards:
            original_price = product.price
            product.price = 0
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'original_price': original_price
        })

    if 'bibbidi-bobbidi-boo' in rewards:
        original_total = total
        total = Decimal(total) * Decimal(0.8)

    grand_total = Decimal(total) + Decimal(delivery)

    context = {
        'basket_items': basket_items,
        'rewards': rewards,
        'original_total': original_total,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
