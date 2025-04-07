from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.conf import settings
from unittest.mock import patch

from ..models import Order, UserProfile, OrderLineItem
from products.models import Product


class OrderModelTests(TestCase):
    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='test',
            email='tesstyuza@test.com',
            password='password123',
        )
        self.user_profile, created = (
            UserProfile.objects.get_or_create(user=self.user)
        )

    def test_order_number_is_generated(self):
        """
        Order number should be generated on save if not provided.
        """
        # Create order.
        order = Order.objects.create(
            user_profile=self.user_profile,
            full_name='Tess Tyuza',
            email=self.user.email,
            street_address_1='Street',
            town_city='Town',
            country='GB'
        )
        # Assertions.
        self.assertTrue(order.order_number.startswith('TU-'))
        self.assertEqual(str(order), order.order_number)
        self.assertEqual(len(order.order_number), 20)

    @patch('checkout.models.Order.lineitems')
    def test_update_total_calculates_correct_totals(self, mock_lineitems):
        """
        update_total() should correctly compute order and grand totals.
        """
        # Create order.
        order = Order.objects.create(
            user_profile=self.user_profile,
            full_name='Tess Tyuza',
            email=self.user.email,
            street_address_1='Street',
            town_city='Town',
            country='GB'
        )
        # Mock lineitem total calculation.
        mock_lineitems.aggregate.return_value = {
            'lineitem_total__sum': Decimal('50.00')
        }
        order.update_total()

        # Assertions
        self.assertEqual(order.order_total, Decimal('50.00'))
        self.assertEqual(order.delivery_cost, Decimal(settings.DELIVERY))
        self.assertEqual(
            order.grand_total, Decimal('50.00') + Decimal(settings.DELIVERY)
        )


class OrderLineItemModelTests(TestCase):
    def setUp(self):
        # Create user.
        self.user = User.objects.create_user(
            username='test',
            email='tesstyuza@test.com',
            password='password123',
        )
        self.user_profile, created = (
            UserProfile.objects.get_or_create(user=self.user)
        )
        # Create product.
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product descripton',
            price=10.00,
            stock=1,
            sku='TEST123',
            unique_stock=True
        )
        # Create order.
        self.order = Order.objects.create(
            user_profile=self.user_profile,
            full_name='Tess Tyuza',
            email=self.user.email,
            street_address_1='Street',
            town_city='Town',
            country='GB'
        )

    def test_lineitem_total_calculcation(self):
        """
        Tests the lineitem total calculation and returned string.
        """
        # Create order lineitem.
        order_line_item = OrderLineItem(
            order=self.order,
            product=self.product1,
            quantity=2
        )

        order_line_item.save()

        # Expected results.
        expected_total = self.product1.price * order_line_item.quantity
        expected_str = (
            f'SKU {self.product1.sku} on order {self.order.order_number}'
        )

        # Assertions.
        self.assertEqual(order_line_item.lineitem_total, expected_total)
        self.assertEqual(str(order_line_item), expected_str)
