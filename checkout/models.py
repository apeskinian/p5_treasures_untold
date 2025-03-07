from datetime import datetime
from decimal import Decimal
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Represents a customer's order, storing details such as user profile,
    contact information, delivery address, order totals, and payment details.

    **Fields:**
    - `order_number (CharField)`: A unique, non-editable order identifier.
    - `user_profile (ForeignKey)`: Links to the `UserProfile` model.
    - `full_name (CharField)`: The customer's full name.
    - `email (EmailField)`: The customer's email address.
    - `phone_number (CharField)`: Optional contact number.
    - `street_address_1 (CharField)`: First line of the street address.
    - `street_address_2 (CharField)`: Optional second line of street address.
    - `town_city (CharField)`: City or town of the customer.
    - `county (CharField)`: Optional county field.
    - `postcode (CharField)`: Optional postal code.
    - `country (CountryField)`: Customer's country.
    - `date (DateField)`: The order creation date (auto-generated).
    - `delivery_cost (DecimalField)`: The cost of delivery.
    - `order_total (DecimalField)`: Total cost of items before delivery.
    - `grand_total (DecimalField)`: Total order cost including delivery.
    - `original_basket (TextField)`: Stores the original basket contents.
    - `rewards_used (TextField)`: Stores any rewards applied to the order.
    - `stripe_pid (CharField)`: The Stripe payment ID.

    **Methods:**
    - `_generate_order_number()`: Generates a unique order number with a
      'TU-YYYYMMDD-XXXXXXXX' format.
    - `update_total()`: Recalculates and updates the `grand_total` field.
    - `save()`: Overrides the default save method to ensure an order number
      is generated if missing.
    - `__str__()`: Returns the order number as the string representation of
      the order.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orders'
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address_1 = models.CharField(max_length=80, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    town_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_basket = models.TextField(null=False, blank=False, default='')
    rewards_used = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_number(self):
        """
         Generate a unique order number using UUID with a 'TU' and date prefix.

        **Returns:**
        - A string in the format 'TU-YYYYMMDD-XXXXXXXX', where:
          - 'YYYYMMDD' is the current date.
          - 'XXXXXXXX' is an 8-character uppercase hex from a UUID.
        """
        date_part = datetime.now().strftime('%Y%m%d')
        return f'TU-{date_part}-{uuid.uuid4().hex[:8].upper()}'

    def update_total(self):
        """
        Updates the `grand_total` field when called.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum'] or 0
        self.delivery_cost = Decimal(settings.DELIVERY)
        self.grand_total = (
            self.order_total + self.delivery_cost
        )
        self.save()

    def save(self, *args, **kwargs):
        """
        Overides the standard save method by checking for an order number and
        generating one if not present.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the `order_number` field as a string.

        **Returns:**
        - The `order_number` field as a string.
        """
        return self.order_number


class OrderLineItem(models.Model):
    """
    Represents a line item for an order.

    **Fields:**
    - `order (ForeignKey)`: Links to :model:`checkout.Order`.
    - `product (ForeignKey)`: Links to :model:`products.Product`.
    - `purchase_price (DecimalField)`: The value that the line item was
        purchased for taking into account any active rewards at the time of
        checkout.
    - `quantity (IntegerField)`: The quantity of the product purchased.
    - `lineitem_total (DecimalField)`: The product price multiplied by the
        quantity.

    **Methods:**
    - `save()`: Overrides the default save method to calculate the
        `lineitem_total` value.
    - `__str__()`: Returns the sku and order in an f string representation of
      the orderlineitem.
    """
    order = models.ForeignKey(
        Order, null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    purchase_price = models.DecimalField(
        null=True, blank=True, max_digits=6, decimal_places=2, default=0.00
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Overides the save method and calculates the `lineitem_total` field.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns an f string providing the sku and related order number.

        **Returns:**
        - An f string with the sku and related order number.
        """
        return f'SKU {self.product.sku} on order {self.order.order_number}'
