from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    discounted_total = 0
    product_count = 0
    discount = settings.DISCOUNT
    delivery = settings.DELIVERY

    if discount > 0:
        discounted_total = Decimal(total-(total * discount/100))
        grand_total = discounted_total + delivery
    else:
        grand_total = total + delivery

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
