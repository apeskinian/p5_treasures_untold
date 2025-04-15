from unittest.mock import patch

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from django.urls import reverse

from ..views import (
    update_stock,
    add_to_basket,
    adjust_basket,
    remove_from_basket,
    check_for_cave_of_wonders
)
from products.models import Product


class UpdateStockTest(TestCase):
    def setUp(self):
        """
        Set up request, session and create :model:`products.Product`
        instances for tests.
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

        # Assertions
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

        # Assertions
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

        # Assertions
        self.assertEqual(self.product2.stock, 0)

    def test_session_expiry_set(self):
        """
        Testing session expiry is set to 86400 seconds.
        """
        update_stock(self.request, self.product2, 5)

        # Assertions
        self.assertEqual(self.request.session.get_expiry_age(), 86400)


class ViewBasketTest(TestCase):
    def setUp(self):
        """
        Set up :model:`auth.User` instance and and url for testing.
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

        # Assertions
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_view_basket_authenticated(self):
        """
        Test that an authenticated user can access the basket view.
        """
        # Log in as the test user.
        self.client.login(username='testuser', password='testpassword')
        # Access the basket view.
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'basket/basket.html')
        self.assertEqual(
            response['Cache-Control'], 'no-cache, must-revalidate, no-store'
        )


class AddToBasketTest(TestCase):
    def setUp(self):
        """
        Set up request factory and instances of :model:`products.Product` and
        :model:`auth.User` for tests.
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

        # Assertions.
        self.assertEqual(request.session['return_url'], '/test_return/')
        self.assertEqual(request.session["basket"], {self.product1.id: 2})
        mock_update_stock.assert_called_once_with(request, self.product1, -2)
        mock_check_reward.assert_called_once_with(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_existing_item_to_basket(
        self, mock_check_reward, mock_update_stock
    ):
        """
        Test quantity adjustment by adding a an item to a basket that already
        has that item in it.
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

        # Assertions.
        self.assertEqual(request.session['return_url'], '/test_return/')
        self.assertEqual(request.session["basket"], {self.product1.id: 4})
        mock_update_stock.assert_called_once_with(request, self.product1, -2)
        mock_check_reward.assert_called_once_with(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_item_qty_non_int(self, mock_check_reward, mock_update_stock):
        """
        Test quantity error handling by passing a non integer as the quantity
        value.
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

        # Assertions.
        self.assertTrue(any("Error in quantity" in str(m) for m in messages))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_item_low_stock(self, mock_check_reward, mock_update_stock):
        """
        Test stock control handling by requesting to add more items than there
        are available to the basket.
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

        # Assertions.
        self.assertTrue(any('There are only' in str(m) for m in messages))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_item_no_stock(self, mock_check_reward, mock_update_stock):
        """
        Test stock control handling by requesting to add an item that no longer
        has any stock.
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

        # Assertions.
        self.assertTrue(any(
            'Sorry but this product is currently unavailable.'
            in str(m) for m in messages
        ))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_add_item_error(self, mock_check_reward, mock_update_stock):
        """
        Test error handling for a simulated exception while calling
        `update_stock`.
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

        # Assertions.
        self.assertTrue(any(
            'There was a problem adding'
            in str(m) for m in messages
        ))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')


class UpdateBasketTest(TestCase):
    def setUp(self):
        """
        Set up request factory and instances of :model:`products.Product` and
        :model:`auth.User` for tests.
        """
        # Create request factory.
        self.factory = RequestFactory()
        # Create test products.
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product descripton',
            price=10.00,
            stock=4,
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
    def test_add_item_qtys_non_int(self, mock_check_reward, mock_update_stock):
        """
        Test quantity error handling by passing a non integer as the quantity
        and previous-quantity values.
        """
        for field in ('quantity', 'previous-quantity'):
            with self.subTest(field=field):
                post_data = {
                    'quantity': '1',
                    'previous-quantity': '1',
                    'redirect_url': '/basket/'
                }
            post_data[field] = 'not_an_integer'

            request = self.factory.post(
                reverse('adjust_basket', args=[self.product1.id]),
                post_data
            )
            request.user = self.user
            self._set_session_and_messages(request)
            response = adjust_basket(request, self.product1.id)
            messages = list(get_messages(request))

            # Assertions.
            self.assertTrue(
                any("Error in quantity" in str(m) for m in messages)
            )
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_adjust_item_stocks(self, mock_check_reward, mock_update_stock):
        """
        Test for stock level results using `quantity_option` to control tests.

        **Tests from `quantity_option` values**
        - '8': Testing for not enough stock for the requested new amount.
        - '2': Testing for no change in the quantity.
        - '3': Testing for valid change in quantity.
        - '0': Testing for removal by changing quantity to 0.
        """
        for quantity_option in ['8', '2', '3', '0']:
            # Set request, user, session and get response.
            request = self.factory.post(
                reverse('adjust_basket', args=[self.product1.id]),
                {
                    'quantity': quantity_option,
                    'previous-quantity': '2',
                    'redirect_url': '/basket/'
                }
            )
            request.user = self.user
            self._set_session_and_messages(request)
            response = adjust_basket(request, self.product1.id)
            messages = list(get_messages(request))

            # Assertions.
            if quantity_option == '8':
                self.assertTrue(
                    any('Sorry, the maximum' in str(m) for m in messages)
                )
            elif quantity_option == '2':
                self.assertTrue(
                    any('Basket not adjusted.' in str(m) for m in messages)
                )
            elif quantity_option == '3':
                self.assertTrue(
                    any('quantity updated' in str(m) for m in messages)
                )
            elif quantity_option == '0':
                self.assertTrue(
                    any('removed from basket' in str(m) for m in messages)
                )
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, '/basket/')

    @patch('basket.views.update_stock')
    @patch('basket.views.check_for_cave_of_wonders')
    def test_adjust_item_error(self, mock_check_reward, mock_update_stock):
        """
        Test error handling for a simulated exception while calling
        `update_stock`.
        """
        # Create an exception.
        mock_update_stock.side_effect = Exception("Forced error")
        # Set request, user, session and get response.
        request = self.factory.post(
            reverse('adjust_basket', args=[self.product1.id]),
            {
                'quantity': '2',
                'previous-quantity': '1',
                'redirect_url': '/basket/'
            }
        )
        request.user = self.user
        self._set_session_and_messages(request)
        response = adjust_basket(request, self.product1.id)
        messages = list(get_messages(request))

        # Assertions.
        self.assertTrue(any(
            'There was a problem adjusting'
            in str(m) for m in messages
        ))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basket/')


class RemoveFromBasket(TestCase):
    def setUp(self):
        """
        Set up request factory and instances of :model:`products.Product` and
        :model:`auth.User` for tests.
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
    def test_delete_item(self, mock_check_reward, mock_update_stock):
        """
        Test for deleting an item using the `quantity` context to control
        a simulated errror for exception handling.

        **Test Options**
        '2': Simulates a valid number.
        'E': Simulates a non integer to simulate an Exception.
        """
        for test in ['2', 'E']:
            # Set request, user, session and get response.
            request = self.factory.post(
                reverse('remove_from_basket', args=[self.product1.id]),
                {
                    'quantity': test
                }
            )
            request.user = self.user
            self._set_session_and_messages(request)
            request.session["basket"] = {str(self.product1.id): 2}
            request.session.save()
            response = remove_from_basket(request, self.product1.id)
            messages = list(get_messages(request))

            # Assertions.
            if test == '2':
                self.assertTrue(any(
                    'removed from basket'
                    in str(m) for m in messages
                ))
                mock_update_stock.assert_called_once_with(
                    request, self.product1, 2
                )
            elif test == 'E':
                self.assertTrue(any(
                    'Error removing item:'
                    in str(m) for m in messages
                ))
            self.assertEqual(response.status_code, 200)


class CheckCaveOfWondersTest(TestCase):
    def setUp(self):
        """
        Set up request, session and :model:`products.Product` instances
        for test.
        """
        # Create request.
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        self.request.session = {}
        # Create products.
        self.monkey_idol = Product.objects.create(
            id=1,
            name='monkey_idol',
            description='product descripton',
            sku='TU-AGR-SMIOA-U-A85D',
            price=10.00,
            stock=1,
        )
        self.beetle_left = Product.objects.create(
            id=2,
            name='beetle_left',
            description='product descripton',
            sku='TU-AGR-LHOAGSB-U-A39A',
            price=10.00,
            stock=1,
        )
        self.beetle_right = Product.objects.create(
            id=3,
            name='beetle_right',
            description='product descripton',
            sku='TU-AGR-RHOAGSB-U-9B7C',
            price=10.00,
            stock=1,
        )

    @patch('basket.views.activate_reward')
    def test_activates_with_both_scarab_halves(self, mock_activate_reward):
        """
        Activates reward when both scarab halves are present
        and idol is absent.
        """
        self.request.session['basket'] = {
            str(self.beetle_left.id):  1,
            str(self.beetle_right.id):  1,
        }
        check_for_cave_of_wonders(self.request)

        # Assertions
        mock_activate_reward.assert_called_once_with(
            self.request, 'activate', 'cave-of-wonders'
        )

    @patch('basket.views.activate_reward')
    def test_deactivates_with_one_scarab_half(self, mock_activate_reward):
        """
        Deactivates reward if only one scarab half is present.
        """
        self.request.session['basket'] = {
            str(self.beetle_left.id):  1,
        }
        check_for_cave_of_wonders(self.request)

        # Assertions
        mock_activate_reward.assert_called_once_with(
            self.request, 'deactivate', 'cave-of-wonders'
        )

    @patch('basket.views.activate_reward')
    def test_deactivates_reward_with_idol_present(self, mock_activate_reward):
        """
        Deactivates reward if the idol is present.
        """
        self.request.session['basket'] = {
            str(self.beetle_left.id):  1,
            str(self.beetle_right.id):  1,
            str(self.monkey_idol.id):  1,
        }
        check_for_cave_of_wonders(self.request)

        # Assertions
        mock_activate_reward.assert_called_once_with(
            self.request, 'deactivate', 'cave-of-wonders', 'infidels'
        )
