from unittest.mock import Mock

from django.contrib.admin.sites import AdminSite
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.test import RequestFactory, TestCase

from ..admin import clear_rewards, empty_basket
from products.models import Product


class EmptyBasketAdminActionTest(TestCase):
    def setUp(self):
        """
        Set up request, sessions and instances of :model:`products.Product`
        for tests.
        """
        # Create a mock request and admin instance.
        self.factory = RequestFactory()
        self.admin_site = AdminSite()
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
        self.product3 = Product.objects.create(
            id=3,
            name='test product 3',
            description='product descripton',
            price=10.00,
            stock=1,
        )
        self.product4 = Product.objects.create(
            id=4,
            name='test product 4',
            description='product descripton',
            price=14.00,
            stock=25
        )

        # Create test sessions with basket contents
        self.session1 = SessionStore()
        self.session1['basket'] = {'1': 1, '2': 2}
        self.session1.save()

        self.session2 = SessionStore()
        self.session2['basket'] = {'3': 1, '4': 5}
        self.session2.save()

        # Sesson 3 for testing more than one unique stock
        self.session3 = SessionStore()
        self.session3['basket'] = {'1': 2}
        self.session3.save()

        # Sesson 4 for testing negative stock
        self.session4 = SessionStore()
        self.session4['basket'] = {'3': -5}
        self.session4.save()

        # Retrieve stored sessions
        self.session_obj1 = (
            Session.objects.get(session_key=self.session1.session_key)
        )
        self.session_obj2 = (
            Session.objects.get(session_key=self.session2.session_key)
        )
        self.session_obj3 = (
            Session.objects.get(session_key=self.session3.session_key)
        )
        self.session_obj4 = (
            Session.objects.get(session_key=self.session4.session_key)
        )

        # Mock request with session key matching session1
        self.request = self.factory.post('/admin/')
        self.request.session = self.session1
        self.request.session.save()

        # Mock modeladmin object
        self.modeladmin = Mock()

    def test_emptying_basket_items(self):
        """
        Testing for successful stock replenishment from basket items stored
        in session.
        """
        queryset = [self.session_obj1, self.session_obj2]
        empty_basket(self.modeladmin, self.request, queryset)

        # Check product stock
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()
        self.product3.refresh_from_db()
        self.product4.refresh_from_db()

        # Assertions
        self.assertEqual(self.product1.stock, 1)
        self.assertEqual(self.product2.stock, 5)
        self.assertEqual(self.product3.stock, 2)
        self.assertEqual(self.product4.stock, 30)

        # Reload sessions
        self.session_obj1 = (
            Session.objects.get(session_key=self.session1.session_key)
        )
        self.session_obj2 = (
            Session.objects.get(session_key=self.session2.session_key)
        )

        store1 = SessionStore(session_key=self.session_obj1.session_key)
        store2 = SessionStore(session_key=self.session_obj2.session_key)

        # Assertions
        self.assertNotIn('basket', store1.load())
        self.assertNotIn('basket', store2.load())
        self.assertNotIn('basket', self.request.session)
        self.modeladmin.message_user.assert_called_once_with(
            self.request,
            'Selected basket(s) have been cleared. Stock has been recovered.'
        )

    def test_catching_unique_stock_more_than_one(self):
        """
        Test to see if unique stock error checking raised the value error
        before passing on it.
        """
        queryset = [self.session_obj3]
        try:
            empty_basket(self.modeladmin, self.request, queryset)
        except ValueError:
            self.fail('ValueError was raised')
        self.product1.refresh_from_db()

        # Assertion
        self.assertEqual(self.product1.stock, 1)

    def test_catching_stock_less_than_zero(self):
        """
        Test to see if the error checking raised a value error for negative
        stock before passing on it.
        """
        queryset = [self.session_obj4]
        try:
            empty_basket(self.modeladmin, self.request, queryset)
        except ValueError:
            self.fail('ValueError was raised')
        self.product3.refresh_from_db()

        # Assertion
        self.assertEqual(self.product3.stock, 0)


class ClearRewardsAdminActionTest(TestCase):
    def setUp(self):
        """
        Set up request and sessions for testing.
        """
        self.factory = RequestFactory()
        self.admin_site = AdminSite()

        # Create two test sessions with rewards
        self.session1 = SessionStore()
        self.session1['rewards'] = 'magic-lamp'
        self.session1.save()

        self.session2 = SessionStore()
        self.session2['rewards'] = 'bibbidi-bobbidi-boo'
        self.session2.save()

        # Retrieve stored sessions
        self.session_obj1 = (
            Session.objects.get(session_key=self.session1.session_key)
        )
        self.session_obj2 = (
            Session.objects.get(session_key=self.session2.session_key)
        )

        # Mock request with session key matching session1
        self.request = self.factory.post('/admin/')
        self.request.session = self.session1
        self.request.session.save()

        # Mock modeladmin object
        self.modeladmin = Mock()

    def test_clear_rewards(self):
        """
        Test to see if rewards are successfully removed from sesion data.
        """
        # Call the action
        queryset = [self.session_obj1, self.session_obj2]
        clear_rewards(self.modeladmin, self.request, queryset)

        # Reload sessions
        self.session_obj1 = (
            Session.objects.get(session_key=self.session1.session_key)
        )
        self.session_obj2 = (
            Session.objects.get(session_key=self.session2.session_key)
        )

        store1 = SessionStore(session_key=self.session_obj1.session_key)
        store2 = SessionStore(session_key=self.session_obj2.session_key)

        # Asssertions
        self.assertNotIn('rewards', store1.load())
        self.assertNotIn('rewards', store2.load())
        self.assertNotIn('rewards', self.request.session)
        self.modeladmin.message_user.assert_called_with(
            self.request, 'Reward data has been cleared for selected sessions.'
        )
