import json
from unittest.mock import patch

from django.test import TestCase, RequestFactory

from ..webhooks import webhook


class WebhooksTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('stripe.Webhook.construct_event')
    def test_handle_unhandled_event(self, mock_construct_event):
        """
        Testing the webhook handler for a generic event.
        """
        event_payload = {
            'type': 'some_unhandled_event',
            'data': {
                'object': {}
            }
        }

        mock_construct_event.return_value = event_payload

        request = self.factory.post(
            '/webhook/',
            data=json.dumps(event_payload),
            content_type='application/json'
        )
        request.META['HTTP_STRIPE_SIGNATURE'] = 'your_stripe_signature'

        response = webhook(request)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn('TU Unhandled webhook:', response.content.decode())

    @patch('stripe.Webhook.construct_event')
    def test_handle_value_error(self, mock_construct_event):
        """
        Simulating a `ValueError` in the payload.
        """
        mock_construct_event.side_effect = ValueError('Invalid payload')

        request = self.factory.post(
            '/webhook/',
            data={},
            content_type='application/json'
        )
        request.META['HTTP_STRIPE_SIGNATURE'] = 'test_signature'

        response = webhook(request)

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid payload', response.content.decode())

    @patch('stripe.Webhook.construct_event')
    def test_handle_generic_exception(self, mock_construct_event):
        """
        Simulating an `Exception` in the payload.
        """
        mock_construct_event.side_effect = Exception('Something went wrong')

        request = self.factory.post(
            '/webhook/',
            data={},
            content_type='application/json'
        )
        request.META['HTTP_STRIPE_SIGNATURE'] = 'test_signature'

        response = webhook(request)

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertIn('Something went wrong', response.content.decode())
