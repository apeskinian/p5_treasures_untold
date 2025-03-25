from django.contrib.admin.sites import site
from django.test import RequestFactory, TestCase
from unittest.mock import MagicMock

from products.models import Product
from ..admin import clear_rewards, empty_basket


class EmptyBasketAdminActionTest(TestCase):
    def setUp(self):
        """
        Set up request, realm and products for test.
        """
        # Create a mock request and admin instance.
        self.factory = RequestFactory()
        self.admin_site = site
        self.modeladmin = MagicMock()

        # Create test products
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product descripton',
            price=10.00,
            stock=0,
            unique_stock=True
        )
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            description='product descripton',
            price=14.00,
            stock=3
        )

    def test_emptying_basket_items(self):
        """
        Testing for successful stock replenishment from basket items stored
        in session.
        """
        request = self.factory.get('/')
        request.session = {'basket': {'1': 1, '2': 2}}

        empty_basket(self.modeladmin, request, None)

        self.product1.refresh_from_db()
        self.product2.refresh_from_db()
        self.assertEqual(self.product1.stock, 1)
        self.assertEqual(self.product2.stock, 5)

        self.assertNotIn('basket', request.session)

        self.modeladmin.message_user.assert_called_once_with(
            request,
            'Selected basket(s) have been cleared. Stock has been recovered.'
        )

    def test_catching_unique_stock_more_than_one(self):
        """
        Test to see if unique stock error checking raised the value error
        before passing on it.
        """
        request = self.factory.get('/')
        request.session = {'basket': {'1': 2}}
        try:
            empty_basket(self.modeladmin, request, None)
        except ValueError:
            self.fail('ValueError was raised')

    def test_catching_stock_less_than_zero(self):
        """
        Test to see if the error checking raised a value error for negative
        stock before passing on it.
        """
        request = self.factory.get('/')
        request.session = {'basket': {'1': -2}}
        try:
            empty_basket(self.modeladmin, request, None)
        except ValueError:
            self.fail('ValueError was raised')


class ClearRewardsAdminActionTest(TestCase):
    def setUp(self):
        """
        Set up request and admin instance for test.
        """
        self.factory = RequestFactory()
        self.admin_site = site
        self.modeladmin = MagicMock()

    def test_removing_rewards_from_session(self):
        """
        Test if 'rewards' is successfully removed from session data.
        """
        request = self.factory.get('/')
        request.session = {'rewards': ['magic-lamp']}

        clear_rewards(self.modeladmin, request, None)

        self.assertNotIn('rewards', request.session)

        self.modeladmin.message_user.assert_called_once_with(
            request, 'Reward data has been cleared for selected sessions.'
        )
