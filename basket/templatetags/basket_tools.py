from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculates the subtotal of a product based on its price and quantity.

    **Arguments:**
    - 'price' (Decimal or float): The price of a single unit of the product.
    - 'quantity' (int): The number of units of the product.

    **Returns:**
    - Decimal or float: The total cost (price * quantity).
    """
    return price * quantity
