from django.contrib.auth.models import User
from django.test import TestCase
from unittest.mock import patch


from ..models import Order, UserProfile, Product, OrderLineItem


class SignalTests(TestCase):
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
        # Used for testing unique stock recovery.
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product descripton',
            price=10.00,
            stock=1,
            unique_stock=True
        )
        # Used for testing normal stock recovery.
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            description='product descripton',
            price=10.00,
            stock=4,
        )
        # Used for catching negative stock recovery.
        self.product3 = Product.objects.create(
            id=3,
            name='test product 3',
            description='product descripton',
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
        # Save the OrderLineItem and check if update_total is called
        self.order_line_item.save()

        # Assert that the update_total method was called on the related order
        mock_update_total.assert_called_once()

    @patch('checkout.models.Order.update_total')
    def test_update_total_on_delete(self, mock_update_total):
        # Delete the OrderLineItem and check if update_total is called
        self.order_line_item.delete()

        # Assert that the update_total method was called on the related order
        mock_update_total.assert_called_once()

    def test_clear_basket(self):
        """
        Tests the stock recovery on user logout.
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

        # Confirm session has the data.
        self.assertIn('basket', self.client.session)
        self.assertIn('rewards', self.client.session)

        # Logout to trigger signal.
        self.client.logout()

        # Refresh session.
        session = self.client.session

        # Check that session data is cleared.
        self.assertNotIn('basket', session)
        self.assertNotIn('rewards', session)

        # Check product stock is recovered.
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()
        self.product3.refresh_from_db()
        # Test for unique stock recovery so stock cannot exceed 1.
        self.assertEqual(self.product1.stock, 1)
        # Test normal stock recovery.
        self.assertEqual(self.product2.stock, 6)
        # Test negative stock error catching.
        self.assertEqual(self.product3.stock, 0)
