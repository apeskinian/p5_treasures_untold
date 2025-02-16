from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    discounted_total = 0
    product_count = 0
    discount = settings.DISCOUNT
    delivery = settings.DELIVERY
    basket = request.session.get('basket', {})
    rewards = request.session.get('rewards', [])
    print(rewards)

    for index, (item_id, quantity) in enumerate(basket.items()):
        product = get_object_or_404(Product, pk=item_id)
        if index < 3 and 'magic-lamp' in rewards:
            product.price = 0
        if product.realm.name == 'Agrabah' and 'cave-of-wonders' in rewards:
            product.price = 0
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # OLD DISCOUNT SYSTEM
    # if discount > 0:
    #     discounted_total = (
    #         Decimal(total) - (Decimal(total) * Decimal(discount) / 100)
    #     )
    #     grand_total = discounted_total + Decimal(delivery)
    # else:
    #     grand_total = Decimal(total) + Decimal(delivery)

    # Look for rewards and apply

    if 'bibbidi-bobbidi-boo' in rewards:
        total = Decimal(total) * Decimal(0.8)

    grand_total = Decimal(total) + Decimal(delivery)

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'delivery': delivery,
        'discounted_total': discounted_total,
        'grand_total': grand_total
    }

    return context
