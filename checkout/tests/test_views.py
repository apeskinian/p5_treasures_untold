import json
from unittest.mock import patch

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, Client
from django.urls import reverse

from profiles.models import UserProfile
from products.models import Product, Realm

from ..models import Order, OrderLineItem


class CachCheckoutTests(TestCase):
    def setUp(self):
        """
        Create client, url and instance of :model:`auth.User` for tests.
        """
        self.client = Client()
        self.user = User.objects.create(
            username='TessTyuza',
            password='testpass',
            email='tess@tyuza.com'
        )
        self.url = reverse('cache_checkout_data')

    def _add_session_data(self, request):
        """
        Add session to the request.
        """
        middleware = SessionMiddleware(get_response=lambda x: x)
        middleware.process_request(request)
        request.session.save()

    @patch('checkout.views.stripe.PaymentIntent.modify')
    def test_cache_checkout_data_success(self, mock_modify):
        """
        Test for successful caching of data.
        """
        # Log user in
        self.client.force_login(self.user)

        # Create session with basket and rewards.
        session = self.client.session
        session['basket'] = {'1': 2}
        session['rewards'] = ['magic lamp']
        session.save()
        post_data = {
            'client_secret': 'pi_123456789_secret_abcdef',
            'save_info': 'on',
        }

        response = self.client.post(self.url, data=post_data)

        # Assertions.
        self.assertEqual(response.status_code, 200)
        mock_modify.assert_called_once_with(
            'pi_123456789',
            metadata={
                'basket_contents': json.dumps({'1': 2}),
                'active_rewards': json.dumps(['magic lamp']),
                'session_key': session.session_key,
                'save_info': 'on',
                'current_user': self.user,
            }
        )

    @patch(
            'checkout.views.stripe.PaymentIntent.modify',
            side_effect=Exception('Stripe error')
    )
    def test_cache_checkout_data_failure(self, mock_modify):
        """
        Test exception handling by simulating a stripe error.
        """
        # Log user in.
        self.client.force_login(self.user)

        # Create session with basket and rewards
        session = self.client.session
        session['basket'] = {'1': 2}
        session['rewards'] = ['magic_lamp']
        session.save()

        post_data = {
            'client_secret': 'pi_123456789_secret_abcdef',
            'save_info': 'on',
        }

        # Assertions
        response = self.client.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Stripe error', response.content)


class CheckoutTests(TestCase):
    def setUp(self):
        """
        Create a client, urls and instances of:
        - :model:`auth.User`
        - :model:`products.Realm`
        - :model:`products.Product`
        for tests. User is also logged in.
        """
        self.client = Client()
        self.user = User.objects.create(
            username='TessTyuza',
            password='testpass',
            email='tess@tyuza.com'
        )
        self.checkout_url = reverse('checkout')
        self.products_url = reverse('products')
        # Log user in.
        self.client.force_login(self.user)
        # Create Realm
        self.agrabah = Realm.objects.create(name='Agrabah')
        # Create product.
        self.product1 = Product.objects.create(
            id=1,
            realm=self.agrabah,
            name='test product 1',
            description='product descripton',
            price=10.00,
            stock=8,
            sku='TEST123',
        )

    def test_empty_basket_redirects_to_products_page(self):
        """
        Test that requesting the checkout view with an empty basket redirects
        the user to the products page with a relevant message.
        """
        session = self.client.session
        session['basket'] = {}
        session.save()

        response = self.client.get(self.checkout_url)
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertRedirects(response, self.products_url)
        self.assertTrue(any(
            "There's nothing in your basket at the moment" in str(msg)
            for msg in messages
        ))

    def test_post_with_invalid_form(self):
        """
        Testing form validation for invalid form when checkout is submitted.
        """
        session = self.client.session
        session['basket'] = {'1': 4}
        session.save()

        response = self.client.post(self.checkout_url, {
            'full_name': '',
            'email': '',
            'phone_number': '',
            'street_address_1': '',
            'street_address_2': '',
            'town_city': '',
            'county': '',
            'postcode': '',
            'country': '',
            'client_secret': 'pi_123456789_secret_abc123',
        })
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertRedirects(response, self.checkout_url)
        self.assertTrue(any(
            "There was an error with your form." in str(msg)
            for msg in messages
        ))

    def test_post_with_valid_form_and_rewards(self):
        """
        Test for successful checkout process.
        """
        session = self.client.session
        session['basket'] = {'1': 4}
        session['rewards'] = [
            'bibbidi-bobbidi-boo',
            'magic-lamp',
            'cave-of-wonders'
        ]
        session.save()

        response = self.client.post(self.checkout_url, {
            'full_name': 'Tess Tyuza',
            'email': 'tess@tyuza.com',
            'phone_number': '',
            'street_address_1': 'Street',
            'street_address_2': '',
            'town_city': 'Town',
            'county': '',
            'postcode': '',
            'country': 'GB',
            'client_secret': 'pi_123456789_secret_abc123',
        })

        # Assertions
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderLineItem.objects.count(), 1)
        order = Order.objects.first()
        self.assertRedirects(
            response, reverse('checkout_success', args=[order.order_number])
        )

    def test_post_with_exception_product_does_not_exist(self):
        """
        Testing error handling by simulating a `DoesNotExist` exception for
        the `get_object_or_404` method.
        """
        session = self.client.session
        session['basket'] = {'1': 4}
        session.save()

        with patch(
            'checkout.views.get_object_or_404',
            side_effect=Product.DoesNotExist()
        ):
            response = self.client.post(self.checkout_url, {
                'full_name': 'Tess Tyuza',
                'email': 'tess@tyuza.com',
                'phone_number': '',
                'street_address_1': 'Street',
                'street_address_2': '',
                'town_city': 'Town',
                'county': '',
                'postcode': '',
                'country': 'GB',
                'client_secret': 'pi_123456789_secret_abc123',
            })
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertRedirects(response, reverse('view_basket'))
        self.assertTrue(any(
            "One of the products in the basket was lost fom our" in str(msg)
            for msg in messages
        ))

    def test_no_profile_exists_shows_empty_form(self):
        """
        Test the checkout page still renders if there is no related instance of
        :model:`profiles.UserProfile` to the logged in user.
        """
        session = self.client.session
        session['basket'] = {'1': 4}
        session.save()

        with patch(
            'profiles.models.UserProfile.objects.get',
            side_effect=UserProfile.DoesNotExist()
        ):
            response = self.client.get(self.checkout_url)

        # Assertions
        self.assertTemplateUsed(response, 'checkout/checkout.html')


class CheckoutSuccessTests(TestCase):
    def setUp(self):
        """
        Create client, url and instances of:
        - :model:`auth.User`
        - :model:`profiles.UserProfile`
        - :model:`checkout.Order`
        for tests.
        """
        # Create client, user and urls.
        self.client = Client()
        self.user = User.objects.create(
            username='TessTyuza',
            password='testpass',
            email='tess@tyuza.com'
        )
        self.profile, created = (
            UserProfile.objects.get_or_create(user=self.user)
        )
        # Log user in.
        self.client.force_login(self.user)
        # Create Order
        self.order = Order.objects.create(
            order_number='12345',
            user_profile=self.profile,
            full_name='Tess Tyuza',
            email='tess@tyuza.com',
            street_address_1='Street',
            town_city='Town',
            country='GB',
            delivery_cost=10.00,
            order_total=100.00,
            grand_total=110.00
        )
        self.success_url = reverse(
            'checkout_success', args=[self.order.order_number]
        )

    def test_checkout_success_view_valid_order_and_saved_profile_details(self):
        """
        Test that a successful checkout with the `save_info` set to True will
        update the users profile with the delivery info set during checkout.
        """
        session = self.client.session
        session['basket'] = {'1': 2}
        session['save_info'] = True
        session.save()

        response = self.client.get(self.success_url)
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertTrue(any(
            'Order successfully processed!' in str(msg)
            for msg in messages
        ))
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_full_name, self.order.full_name)
        self.assertEqual(self.profile.default_town_city, self.order.town_city)
