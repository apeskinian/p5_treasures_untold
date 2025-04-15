from decimal import Decimal
from unittest.mock import patch, MagicMock

from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.test import TestCase, Client, RequestFactory

from products.models import Product, Realm
from profiles.models import UserProfile

from ..webhook_handler import StripeWH_Handler


class DotDict(dict):
    """
    A dictionary that allows dot notation access. Used to simulate a data
    structure similar to that sent by Stripe so that dot notation can be used
    to access data.
    """
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]


def dot_dict(d):
    """
    Recursively convert dictionary to DotDict.
    """
    if isinstance(d, dict):
        d = {
            k: dot_dict(v) if isinstance(v, dict) else v for k, v in d.items()
        }
        return DotDict(d)
    return d


class StripeHandlerTests(TestCase):
    @patch('checkout.webhook_handler.stripe.Charge.retrieve')
    @patch('checkout.webhook_handler.send_mail')
    def test_handle_payment_intent_succeeded_order_not_found(
        self, mock_send_mail, mock_charge_retrieve
    ):
        """
        Testing order creation from webhook when order cannot be found from
        view creation. This also tests removing session data and all three
        rewards. None values in the stripe data are also tested to be replaced
        with ''.
        Instances of:
        - :model:`auth.User`
        - :model:`profiles.UserProfile`
        - :model:`products.Realm`
        - :model:`products.Product`
        are created for the test.
        """
        # Mock request object
        mock_request = MagicMock()
        mock_request.build_absolute_uri.return_value = 'http://example.com'
        # Set up mock charge for Stripe
        mock_charge = MagicMock()
        mock_charge.amount = 1000
        mock_charge.billing_details.email = 'tess@tyuza.com'
        mock_charge.billing_details.name = 'Tess Tyuza'
        mock_charge.latest_charge = 'pidtest'
        mock_charge_retrieve.return_value = mock_charge
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
        self.client.force_login(self.user)
        # Set up test realm and product for magic-lamp reward
        self.agrabah = Realm.objects.create(name='Agrabah')
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            realm=self.agrabah,
            description='product descripton',
            price=10.00,
            stock=3
        )

        # Add basket and rewards to session to test removal from session
        self.session1 = SessionStore()
        self.session1['basket'] = {'1': 1}
        self.session1['rewards'] = ['bibbidi-bobbidi-boo']
        self.session1.save()
        session_key = self.session1.session_key

        # Simulated stripe data
        event_data = {
            'data': {
                'object': {
                    'id': 'pidtest',
                    'metadata': {
                        'basket_contents': '{"1": 1}',
                        'active_rewards': '["magic-lamp", "cave-of-wonders", "bibbidi-bobbidi-boo"]',  # noqa: E501
                        'session_key': session_key,
                        'save_info': 'true',
                        'current_user': 'TessTyuza',
                    },
                    'shipping': {
                        'address': {
                            'line1': 'Street',
                            'line2': '',
                            'city': 'Town',
                            'state': '',
                            'postal_code': '',
                            'country': 'GB',
                        },
                        'phone': '',
                        'name': 'Tess Tyuza',
                    },
                    'latest_charge': 'pidtest',
                }
            },
            'type': 'payment_intent.succeeded'
        }
        # Create dot notation dictionary to simulate info from stripe.
        event_data_dot = dot_dict(event_data)
        # Instantiate the handler
        handler = StripeWH_Handler(request=mock_request)

        # Call the handler method
        response = handler.handle_payment_intent_succeeded(event_data_dot)

        # Check if the email was sent
        mock_send_mail.assert_called_once()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'SUCCESS order created in webhook',
            response.content.decode()
        )

    @patch('checkout.webhook_handler.stripe.Charge.retrieve')
    @patch('checkout.webhook_handler.send_mail')
    def test_handle_payment_intent_succeeded_order_not_found_no_session(
        self, mock_send_mail, mock_charge_retrieve
    ):
        """
        Testing order creation from webhook when order cannot be found from
        view creation. This also checks for the warning that will also be shown
        when no session data can be found to clear.
        Instances of:
        - :model:`auth.User`
        - :model:`profiles.UserProfile`
        - :model:`products.Realm`
        - :model:`products.Product`
        are created for the test.
        """
        # Mock request object
        mock_request = MagicMock()
        mock_request.build_absolute_uri.return_value = 'http://example.com'
        # Set up mock charge for Stripe
        mock_charge = MagicMock()
        mock_charge.amount = 1000
        mock_charge.billing_details.email = 'tess@tyuza.com'
        mock_charge.billing_details.name = 'Tess Tyuza'
        mock_charge.latest_charge = 'pidtest'
        mock_charge_retrieve.return_value = mock_charge
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
        self.client.force_login(self.user)
        # Set up test realm and product for magic-lamp reward
        self.agrabah = Realm.objects.create(name='Agrabah')
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            realm=self.agrabah,
            description='product descripton',
            price=10.00,
            stock=3
        )

        # Simulated stripe data
        event_data = {
            'data': {
                'object': {
                    'id': 'pidtest',
                    'metadata': {
                        'basket_contents': '{"1": 1}',
                        'active_rewards': '[]',
                        'session_key': 'fake_session_key',
                        'save_info': 'true',
                        'current_user': 'TessTyuza',
                    },
                    'shipping': {
                        'address': {
                            'line1': 'Street',
                            'line2': '',
                            'city': 'Town',
                            'state': '',
                            'postal_code': '',
                            'country': 'GB',
                        },
                        'phone': '',
                        'name': 'Tess Tyuza',
                    },
                    'latest_charge': 'pidtest',
                }
            },
            'type': 'payment_intent.succeeded'
        }
        # Create dot notation dictionary to simulate info from stripe.
        event_data_dot = dot_dict(event_data)

        # Instantiate the handler
        handler = StripeWH_Handler(request=mock_request)

        # Call the handler method
        response = handler.handle_payment_intent_succeeded(event_data_dot)

        # Check if the email was sent
        mock_send_mail.assert_called_once()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'SUCCESS order created in webhook',
            response.content.decode()
        )
        self.assertIn(
            'WARNING basket not cleared contact admin.',
            response.content.decode()
        )

    @patch('checkout.webhook_handler.stripe.Charge.retrieve')
    def test_handle_payment_intent_succeeded_user_not_found(
        self, mock_charge_retrieve
    ):
        """
        Testing webhook exception handling for no user profile found. An
        instance of :model:`products.Product` is created for the tests.
        """
        # Set up mock charge for Stripe
        mock_charge = MagicMock()
        mock_charge.amount = 1000
        mock_charge.billing_details.email = 'tess@tyuza.com'
        mock_charge.billing_details.name = 'Tess Tyuza'
        mock_charge.latest_charge = 'pidtest'
        mock_charge_retrieve.return_value = mock_charge
        # Set up test product
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product descripton',
            price=10.00,
            stock=3
        )

        # Simulated stripe data
        event_data = {
            'data': {
                'object': {
                    'id': 'pidtest',
                    'metadata': {
                        'basket_contents': '{"1": 1}',
                        'active_rewards': '[]',
                        'session_key': 'fake_session_key',
                        'save_info': 'true',
                        'current_user': 'NOPROFILE',
                    },
                    'shipping': {
                        'address': {
                            'line1': 'Street',
                            'line2': '',
                            'city': 'Town',
                            'state': '',
                            'postal_code': '',
                            'country': 'GB',
                        },
                        'phone': '',
                        'name': 'Tess Tyuza',
                    },
                    'latest_charge': 'pidtest',
                }
            },
            'type': 'payment_intent.succeeded'
        }
        # Create dot notation dictionary to simulate info from stripe.
        event_data_dot = dot_dict(event_data)

        # Instantiate the handler
        handler = StripeWH_Handler(request=None)

        # Call the handler method
        response = handler.handle_payment_intent_succeeded(event_data_dot)

        # Assertions
        self.assertEqual(response.status_code, 500)
        self.assertIn('User not found', response.content.decode())

    @patch('checkout.webhook_handler.stripe.Charge.retrieve')
    def test_handle_payment_intent_succeeded_product_not_found(
        self, mock_charge_retrieve
    ):
        """
        Testing webhook exception handling for errors in creating the order.
        This test references a product that does not exist. Instances of
        :model:`auth.User` and :model:`profiles.UserProfile` are created for
        the test.
        """
        # Set up mock charge for Stripe
        mock_charge = MagicMock()
        mock_charge.amount = 1000
        mock_charge.billing_details.email = 'tess@tyuza.com'
        mock_charge.billing_details.name = 'Tess Tyuza'
        mock_charge.latest_charge = 'pidtest'
        mock_charge_retrieve.return_value = mock_charge
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
        self.client.force_login(self.user)
        # Simulated stripe data
        event_data = {
            'data': {
                'object': {
                    'id': 'pidtest',
                    'metadata': {
                        'basket_contents': '{"1": 1}',
                        'active_rewards': '[]',
                        'session_key': 'fake_session_key',
                        'save_info': 'true',
                        'current_user': 'TessTyuza',
                    },
                    'shipping': {
                        'address': {
                            'line1': 'Street',
                            'line2': '',
                            'city': 'Town',
                            'state': '',
                            'postal_code': '',
                            'country': 'GB',
                        },
                        'phone': '',
                        'name': 'Tess Tyuza',
                    },
                    'latest_charge': 'pidtest',
                }
            },
            'type': 'payment_intent.succeeded'
        }
        # Create dot notation navigational dictionary to simulate info from
        # stripe.
        event_data_dot = dot_dict(event_data)
        # Instantiate the handler
        handler = StripeWH_Handler(request=None)

        # Call the handler method
        response = handler.handle_payment_intent_succeeded(event_data_dot)

        # Assertions
        self.assertEqual(response.status_code, 500)
        self.assertIn('ERRROR:', response.content.decode())

    @patch('checkout.webhook_handler.stripe.Charge.retrieve')
    @patch('checkout.webhook_handler.send_mail')
    @patch('checkout.webhook_handler.Order.objects.get')
    def test_handle_payment_intent_succeeded_order_exists(
        self, mock_order_get, mock_send_mail, mock_charge_retrieve
    ):
        """
        Test webhook handler seeing an order has been created and so does not
        create one itself, just the email is sent. Instances of
        :model:`auth.User` and :model:`profiles.UserProfile` are created
        for the test.
        """
        # Create mock order data
        mock_order = MagicMock()
        mock_order.stripe_pid = 'pidtest'
        mock_order.full_name = 'Tess Tyuza'
        mock_order.email = 'tess@tyuza.com'
        mock_order.phone_number = '1234567890'
        mock_order.street_address_1 = 'Street'
        mock_order.street_address_2 = ''
        mock_order.town_city = 'Town'
        mock_order.county = 'County'
        mock_order.postcode = '12345'
        mock_order.country = 'GB'
        mock_order.delivery_cost = Decimal(10.00)
        mock_order.order_total = Decimal(100.00)
        mock_order.grand_total = Decimal(100.00)
        mock_order.original_basket = '{"1": 1}'
        mock_order.rewards_used = ''
        # Set up the mock return value for `get`
        mock_order_get.return_value = mock_order
        # Mock request object
        mock_request = MagicMock()
        mock_request.build_absolute_uri.return_value = 'http://example.com'
        # Set up mock charge for Stripe
        mock_charge = MagicMock()
        mock_charge.amount = 10000
        mock_charge.billing_details.email = 'tess@tyuza.com'
        mock_charge.billing_details.name = 'Tess Tyuza'
        mock_charge.latest_charge = 'pidtest'
        mock_charge_retrieve.return_value = mock_charge

        # Create client, user.
        self.client = Client()
        self.user = User.objects.create(
            username='TessTyuza',
            password='testpass',
            email='tess@tyuza.com'
        )
        self.profile, created = (
            UserProfile.objects.get_or_create(user=self.user)
        )
        self.client.force_login(self.user)

        # Simulated stripe data
        event_data = {
            'data': {
                'object': {
                    'id': 'pidtest',
                    'metadata': {
                        'basket_contents': '{"1": 1}',
                        'active_rewards': '',
                        'session_key': 'fake_session_key',
                        'save_info': 'true',
                        'current_user': 'TessTyuza',
                    },
                    'shipping': {
                        'address': {
                            'line1': 'Street',
                            'line2': 'Street',
                            'city': 'Town',
                            'state': 'County',
                            'postal_code': '12345',
                            'country': 'GB',
                        },
                        'phone': '1234567890',
                        'name': 'Tess Tyuza',
                    },
                    'latest_charge': 'pidtest',
                }
            },
            'type': 'payment_intent.succeeded'
        }

        # Create dot notation dictionary to simulate info from stripe.
        event_data_dot = dot_dict(event_data)

        # Instantiate the handler
        handler = StripeWH_Handler(request=mock_request)

        # Call the handler method
        response = handler.handle_payment_intent_succeeded(event_data_dot)

        # Assertions
        mock_send_mail.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Order verified in database', response.content.decode())

    def test_handle_unhandled_event(self):
        """
        Handling a generic event that is not mapped in `webhooks.py`
        """
        self.factory = RequestFactory()
        self.request = self.factory.post('/webhook/')
        self.handler = StripeWH_Handler(request=self.request)
        event = {
            'type': 'some.unhandled.event',
        }

        response = self.handler.handle_event(event)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'TU Unhandled webhook:',
            response.content.decode()
        )

    def test_handle_payment_intent_failed(self):
        """
        Handling a failed stripe payment intent.
        """
        self.factory = RequestFactory()
        self.request = self.factory.post('/webhook/')
        self.handler = StripeWH_Handler(request=self.request)
        event = {
            'type': 'payment_intent.payment_failed',
        }

        response = self.handler.handle_payment_intent_payment_failed(event)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'TU Payment failed:',
            response.content.decode()
        )
