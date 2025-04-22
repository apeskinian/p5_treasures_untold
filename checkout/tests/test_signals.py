from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase

from products.models import Product
from profiles.models import UserProfile

from ..models import Order, OrderLineItem


class SignalTests(TestCase):
    def setUp(self):
        """
        Create instances of:
        - :model:`auth.User`
        - :model:`profiles.UserProfile`
        - :model:`products.Product`
        - :model:`checkout.Order`
        - :model:`checkout.OrderLineItem`
        for tests.
        """
        # Create user.
        self.user = User.objects.create_user(
            username='test',
            email='tesstyuza@test.com',
            password='password123',
        )
        self.user_profile, created = (
            UserProfile.objects.get_or_create(user=self.user)
        )
        # Create products.
        # Used for testing unique stock recovery.
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product description',
            price=10.00,
            stock=1,
            unique_stock=True
        )
        # Used for testing normal stock recovery.
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            description='product description',
            price=10.00,
            stock=4,
        )
        # Used for catching negative stock recovery.
        self.product3 = Product.objects.create(
            id=3,
            name='test product 3',
            description='product description',
            price=10.00,
            stock=2,
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
        # Create an OrderLineItem
        self.order_line_item = OrderLineItem(
            order=self.order,
            product=self.product1,
            quantity=4
        )
        self.order_line_item.save()

    @patch('checkout.models.Order.update_total')
    def test_update_total_on_save(self, mock_update_total):
        """
        Test to check if `update_total()` is called when an instance of
        :model:`checkout.OrderLineItem` is saved.
        """
        self.order_line_item.save()

        # Assertions
        mock_update_total.assert_called_once()

    @patch('checkout.models.Order.update_total')
    def test_update_total_on_delete(self, mock_update_total):
        """
        Test to check if `update_total()` is called when an instance of
        :model:`checkout.OrderLineItem` is deleted.
        """
        self.order_line_item.delete()

        # Assertions
        mock_update_total.assert_called_once()

    def test_clear_basket(self):
        """
        Test for stock recovery control when a user logs out by logging in,
        creating a basket with items in the session and then logging out. This
        also tests for stock error handling for overstocking unique items and
        negative stock events.
        """
        # Login in with user.
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        # Create session and add basket contents and rewards.
        session = self.client.session
        session['basket'] = {'1': 1, '2': 2, '3': -4}
        session['rewards'] = ['magic-lamp']
        session.save()

        # Assertions
        self.assertIn('basket', self.client.session)
        self.assertIn('rewards', self.client.session)

        # Logout to trigger signal.
        self.client.logout()
        # Refresh session.
        session = self.client.session
        # Check product stock is recovered.
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()
        self.product3.refresh_from_db()

        # Assertions
        self.assertNotIn('basket', session)
        self.assertNotIn('rewards', session)
        # Test normal stock recovery.
        self.assertEqual(self.product2.stock, 6)
        # Test for unique stock recovery so stock cannot exceed 1.
        self.assertEqual(self.product1.stock, 1)
        # Test negative stock error catching.
        self.assertEqual(self.product3.stock, 0)
