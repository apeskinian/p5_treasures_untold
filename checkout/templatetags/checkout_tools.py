from decimal import Decimal
from django import template

register = template.Library()


@register.filter(name='calc_original_total')
def calc_original_total(total):
    return total / Decimal(0.8)
