from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch

from products.models import Product
from ..views import update_stock, add_to_basket


class UpdateStockTest(TestCase):
    def setUp(self):
        """
        Set up request, session and products for test.
        """
        # Create request
        self.factory = RequestFactory()

        self.session1 = SessionStore()
        self.session1.save()

        self.request = self.factory.get('/')
        self.request.session = self.session1

        # Create test products
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product descripton',
            price=10.00,
            stock=1,
            unique_stock=True
        )
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            description='product descripton',
            price=10.00,
            stock=5,
        )

    def test_normal_stock_update(self):
        """
        Testing stock adjusment within normal parameters.
        """
        update_stock(self.request, self.product2, 5)
        self.product2.refresh_from_db()
        self.assertEqual(self.product2.stock, 10)

    def test_catching_unique_stock_more_than_one(self):
        """
        Test to see if unique stock error checking raised the value error
        before passing on it.
        """
        try:
            update_stock(self.request, self.product1, 5)
        except ValueError:
            self.fail('ValueError was raised')

        self.product1.refresh_from_db()
        self.assertEqual(self.product1.stock, 1)

    def test_catching_stock_less_than_zero(self):
        """
        Test to see if the error checking raised a value error for negative
        stock before passing on it.
        """
        try:
            update_stock(self.request, self.product2, -10)
        except ValueError:
            self.fail('ValueError was raised')

        self.product2.refresh_from_db()
        self.assertEqual(self.product2.stock, 0)

    def test_session_expiry_set(self):
        """
        Testing session expiry is set to 86400 seconds.
        """
        update_stock(self.request, self.product2, 5)
        self.assertEqual(self.request.session.get_expiry_age(), 86400)


class ViewBasketTest(TestCase):
    def setUp(self):
        """
        Sets up an authenticated user for testing.
        """
        # Create a test user.
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        # URL for the basket view.
        self.url = reverse('view_basket')

    def test_view_basket_requires_login(self):
        """
        Test that the view requires login.
        """
        # Try to access the basket view without logging in.
        response = self.client.get(self.url)
        # Check if it redirects to the login page.
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_view_basket_authenticated(self):
        """
        Test that an authenticated user can access the basket view.
        """
        # Log in as the test user.
        self.client.login(username='testuser', password='testpassword')
        # Access the basket view.
        response = self.client.get(self.url)
        # Check if the response uses the correct template.
        self.assertTemplateUsed(response, 'basket/basket.html')
        # Check for cache control headers.
        self.assertEqual(
            response['Cache-Control'], 'no-cache, must-revalidate, no-store'
        )


class AddToBasketTest(TestCase):
    def setUp(self):
        """
        Set up request, session and products for test.
        """
        # Create request.
        self.factory = RequestFactory()

        # Create test products.
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product descripton',
            price=10.00,
            stock=4,
        )
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            description='product descripton',
            price=10.00,
            stock=0,
        )

        # Create a test user.
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

    def _set_session_and_messages(self, request):
        """
        Helper to add session and messages support to the request.
        """
        # Attach session middleware.
        session_middleware = SessionMiddleware(lambda req: None)
        session_middleware.process_request(request)
        request.session.save()

        # Attach messages framework.
        messages_middleware = MessageMiddleware(lambda req: None)
        messages_middleware.process_request(request)
        setattr(request, '_messages', FallbackStorage(request))

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_new_item_to_basket(
        self, mock_check_reward, mock_update_stock
    ):
        """
        Test adding a new item to an empty basket.
        """
        # Set request, user, session and get response.
        request = self.factory.post(
            reverse('add_to_basket', args=[self.product1.id]),
            {
                'quantity': '2',
                'redirect_url': '/basket/',
                'return_url': '/test_return/'
            }
        )
        request.user = self.user
        self._set_session_and_messages(request)
        response = add_to_basket(request, self.product1.id)

        # Tests assertions.
        # Check return_url.
        self.assertEqual(request.session['return_url'], '/test_return/')
        # Check the item was added.
        self.assertEqual(request.session["basket"], {self.product1.id: 2})
        # Check stock update was called.
        mock_update_stock.assert_called_once_with(request, self.product1, -2)
        # Check cave of wonders was checked.
        mock_check_reward.assert_called_once_with(request)
        # Check the user was redirected correctly.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_existing_item_to_basket(
        self, mock_check_reward, mock_update_stock
    ):
        """
        Test adding a new item to an empty basket.
        """
        # Set request, user, session and get response.
        request = self.factory.post(
            reverse('add_to_basket', args=[self.product1.id]),
            {
                'quantity': '2',
                'redirect_url': '/basket/',
                'return_url': '/test_return/'
            }
        )
        request.user = self.user
        self._set_session_and_messages(request)
        request.session["basket"] = {self.product1.id: 2}
        request.session.save()
        response = add_to_basket(request, self.product1.id)

        # Tests assertions.
        # Check return_url.
        self.assertEqual(request.session['return_url'], '/test_return/')
        # Check the item was added.
        self.assertEqual(request.session["basket"], {self.product1.id: 4})
        # Check stock update was called.
        mock_update_stock.assert_called_once_with(request, self.product1, -2)
        # Check cave of wonders was checked.
        mock_check_reward.assert_called_once_with(request)
        # Check the user was redirected correctly.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_item_qty_non_int(self, mock_check_reward, mock_update_stock):
        """
        Test errors in quantity.
        """
        # Set request, user, session and get response.
        request = self.factory.post(
            reverse('add_to_basket', args=[self.product1.id]),
            {
                'quantity': 'not_an_integer',
                'redirect_url': '/basket/'
            }
        )
        request.user = self.user
        self._set_session_and_messages(request)
        response = add_to_basket(request, self.product1.id)
        messages = list(get_messages(request))

        # Tests assertions.
        # Ensure an error message was added.
        self.assertTrue(any("Error in quantity" in str(m) for m in messages))
        # Ensure it redirects.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_item_low_stock(self, mock_check_reward, mock_update_stock):
        """
        Test for not enough stock.
        """
        # Set request, user, session and get response.
        request = self.factory.post(
            reverse('add_to_basket', args=[self.product1.id]),
            {
                'quantity': '6',
                'redirect_url': '/basket/'
            }
        )
        request.user = self.user
        self._set_session_and_messages(request)
        response = add_to_basket(request, self.product1.id)
        messages = list(get_messages(request))

        # Tests assertions.
        # Ensure an error message was added.
        self.assertTrue(any('There are only' in str(m) for m in messages))
        # Ensure it redirects.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_item_no_stock(self, mock_check_reward, mock_update_stock):
        """
        Test for not enough stock.
        """
        # Set request, user, session and get response.
        request = self.factory.post(
            reverse('add_to_basket', args=[self.product2.id]),
            {
                'quantity': '6',
                'redirect_url': '/basket/'
            }
        )
        request.user = self.user
        self._set_session_and_messages(request)
        response = add_to_basket(request, self.product2.id)
        messages = list(get_messages(request))

        # Tests assertions.
        # Ensure an error message was added.
        self.assertTrue(any(
            'Sorry but this product is currently unavailable.'
            in str(m) for m in messages
        ))
        # Ensure it redirects.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock', side_effect=Exception('ERROR'))
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_item_error(self, mock_check_reward, mock_update_stock):
        """
        Test for not error adding to the basket.
        """
        # Create an exception.
        mock_update_stock.side_effect = Exception("Forced error")
        # Set request, user, session and get response.
        request = self.factory.post(
            reverse('add_to_basket', args=[self.product1.id]),
            {
                'quantity': '2',
                'redirect_url': '/basket/'
            }
        )
        request.user = self.user
        self._set_session_and_messages(request)
        response = add_to_basket(request, self.product1.id)
        messages = list(get_messages(request))

        # Tests assertions.
        # Ensure an error message was added.
        self.assertTrue(any(
            'There was a problem adding'
            in str(m) for m in messages
        ))
        # Ensure it redirects.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')
