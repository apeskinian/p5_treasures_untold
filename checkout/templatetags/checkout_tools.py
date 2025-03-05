from decimal import Decimal

from django import template

register = template.Library()


@register.filter(name='calc_original_total')
def calc_original_total(total):
    """
    This filter calculates the original total price before applying a 20%
    discount.

    **Args:**
    - 'total': The total price after the 20% discount.

    **Returns:**
    - Decimal: The original total price before the discount was applied.
    """
    return total / Decimal(0.8)
