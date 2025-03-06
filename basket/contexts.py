from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product


def basket_contents(request):
    """
    Provide global access to the basket contents across the app

    **Context:**
    - `basket_items`: A list of dictionaries containing the followingf keys:
        - `item_id`: the pk of a product
        - `quantity`: the quantity of the product
        - `product`: an instance of the product
        - `original price`: a copy of the original product instance price
    - `rewards`: A list containing any current activated rewards.
    - `original_total`: A float copy of the accumulated total before any
        discounts are applied.
    - `total`: A float of the total after any discounts are applied.
    - `product_count`: An integer of the number of items in the basket.
    - `delivery`: A float for the delivery cost defined in settings.py.
    - `grand_total`: A float calculated from the total and delivery cost.

    **Returns:**
    A context dictionary containing:
    - `basket_items`
    - `rewards`
    - `original_price`
    - `total`
    - `product_count`
    - `delivery`
    - `grand_total`
    """
    basket_items = []
    total = 0
    product_count = 0
    delivery = settings.DELIVERY
    basket = request.session.get('basket', {})
    rewards = request.session.get('rewards', [])
    original_total = 0

    for index, (item_id, quantity) in enumerate(basket.items()):
        product = get_object_or_404(Product, pk=item_id)
        original_price = product.price
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
