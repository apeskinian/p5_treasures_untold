from datetime import timedelta
from unittest.mock import MagicMock, patch

from django.contrib.messages import get_messages
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from ..models import Subscriber
from ..views import generate_confirmation_token


class GenerateConfirmationTokenTests(TestCase):
    def test_confirmation_token_generation(self):
        """
        Create instance of :model:`support.Subscriber` and request token using
        that instance. Confirm token is generated.
        """
        subscriber = Subscriber.objects.create(email='tess@tyuza.com')
        token = generate_confirmation_token(subscriber)

        # Assertions
        self.assertIsInstance(token, str)
        self.assertTrue(token)


class FaqTests(TestCase):
    def test_faq_view(self):
        """
        Testing the faq view.
        """
        self.client = Client()
        self.url = reverse('faq')
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'support/support.html')
        self.assertEqual(response.context['title'], 'FAQs')


class ContactTests(TestCase):
    def test_contact_form_get(self):
        """
        Testing the contact view.
        """
        self.client = Client()
        self.url = reverse('contact')
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'support/support.html')
        self.assertEqual(response.context['title'], 'Contact Us')

    @patch('support.views.send_mail')
    def test_contact_form_post_valid_form(self, mock_send_mail):
        """
        Testing posting the contact us form.
        """
        self.client = Client()
        self.url = reverse('contact')
        mock_request = MagicMock()
        mock_request.build_absolute_uri.return_value = 'http://example.com'

        response = self.client.post(
            self.url,
            {
                'name': 'Tess Tyuza',
                'email': 'tess@tyuza.com',
                'message': 'Test messsage.'
            })

        # Assertions
        self.assertTemplateUsed(response, 'support/support.html')
        self.assertEqual(response.context['title'], 'Thank You')
        mock_send_mail.assert_called_once()

    def test_contact_form_post_invalid_form(self):
        """
        Testing posting an invalid contact us form.
        """
        self.client = Client()
        self.url = reverse('contact')

        response = self.client.post(
            self.url,
            {
                'name': 'Tess Tyuza',
                'email': 'tess@tyuza.com',
                'message': ''
            })
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'There was a problem sending your message' in str(msg)
            for msg in messages
        ))
        self.assertTemplateUsed(response, 'support/support.html')
        self.assertEqual(response.context['title'], 'Contact Us')


class NewsletterTests(TestCase):
    def test_newsletter_view(self):
        """
        Testing the newsletter view.
        """
        self.client = Client()
        self.url = reverse('newsletter')
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'support/support.html')
        self.assertEqual(response.context['title'], 'Newsletter')


class SubscribeTests(TestCase):
    @patch('support.views.send_mail')
    def test_subscription_request_success(
        self, mock_send_email
    ):
        """
        Testing the submission of the newsletter form.
        """
        self.client = Client()
        self.url = reverse('subscribe')
        mock_request = MagicMock()
        mock_request.build_absolute_uri.return_value = 'http://example.com'

        response = self.client.post(
            self.url,
            {'newsletter-email': 'tess@tyuza.com'},
            HTTP_REFERER='http://example.com/origin/'
        )
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'Thank you for subscribing!' in str(msg)
            for msg in messages
        ))
        mock_send_email.assert_called_once()

    def test_subscription_request_with_already_active_email(self):
        """
        Testing the submission of the newsletter form with an email that is
        already marked as active. An instance of :model:`support.Subscriber`
        is created for this test.
        """
        self.client = Client()
        self.url = reverse('subscribe')
        subscriber = Subscriber.objects.create(
            email='tess@tyuza.com',
            is_active=True
        )

        response = self.client.post(
            self.url,
            {'newsletter-email': 'tess@tyuza.com'},
            HTTP_REFERER='http://example.com/origin/'
        )
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(subscriber.is_active)
        self.assertTrue(any(
            'This email has already been subscribed' in str(msg)
            for msg in messages
        ))

    def test_subscription_request_with_invalid_email(self):
        """
        Testing the submission of the newsletter form with an email that is
        invalid.
        """
        self.client = Client()
        self.url = reverse('subscribe')

        response = self.client.post(
            self.url,
            {'newsletter-email': 'tesstyuza.com'},
            HTTP_REFERER='http://example.com/origin/'
        )
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'Please ensure the form is valid:' in str(msg)
            for msg in messages
        ))


class ConfirmSubscriptionTests(TestCase):
    def test_successful_subscription_confirmation(self):
        """
        Tests a confirmation attempt with a token within the expiry time. An
        instance of :model:`support.Subscriber` is created for this test.
        """
        token_creation = timezone.now()
        subscriber = Subscriber.objects.create(
            id=1,
            email='Tess@Tyuza.com',
            token='test-token',
            token_created_at=token_creation,
        )
        self.client = Client()
        self.url = reverse(
            'confirm_subscription',
            args=[subscriber.id, subscriber.token]
        )

        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'support/support.html')
        self.assertEqual(response.context['title'], 'Success')

    def test_subscription_confirmation_with_expired_token(self):
        """
        Tests a confirmation attempt with a token that has expired. An
        instance of :model:`support.Subscriber` is created for this test.
        """
        token_creation = timezone.now() - timedelta(days=3)
        subscriber = Subscriber.objects.create(
            id=1,
            email='Tess@Tyuza.com',
            token='test-token',
            token_created_at=token_creation,
        )
        self.client = Client()
        self.url = reverse(
            'confirm_subscription',
            args=[subscriber.id, subscriber.token]
        )

        response = self.client.get(self.url)
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'Your confirmation link has expired, please try again.' in str(msg)
            for msg in messages
        ))
        self.assertRedirects(response, reverse('newsletter'))
        self.assertFalse(Subscriber.objects.filter(id=subscriber.id).exists())

    def test_subscription_confirmation_with_invalid_token(self):
        """
        Tests a confirmation attempt with an invalid token. An
        instance of :model:`support.Subscriber` is created for this test.
        """
        token_creation = timezone.now()
        subscriber = Subscriber.objects.create(
            id=1,
            email='Tess@Tyuza.com',
            token='test-token',
            token_created_at=token_creation,
        )
        self.client = Client()
        self.url = reverse(
            'confirm_subscription',
            args=[subscriber.id, 'wrong-token']
        )

        response = self.client.get(self.url)
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'Invalid token' in str(msg)
            for msg in messages
        ))
        self.assertRedirects(response, reverse('newsletter'))


class ConfirmUnsubscriptionTests(TestCase):
    def setUp(self):
        """
        Create client and instance of :model:`support.Subscriber` for tests.
        """
        self.client = Client()
        self.subscriber = Subscriber.objects.create(
            id=1,
            email='Tess@Tyuza.com',
            token='test-token',
        )

    def test_unsubscribe_with_valid_token(self):
        """
        Testing a successful unsubscription.
        """
        response = self.client.get(
            reverse(
                'confirm_unsubscription',
                args=[self.subscriber.id, self.subscriber.token]
            )
        )
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'You have been unsubscribed' in str(msg)
            for msg in messages
        ))

    def test_unsubscribe_with_invalid_token(self):
        """
        Testing an unsuccessful unsubscription.
        """
        response = self.client.get(
            reverse(
                'confirm_unsubscription',
                args=[self.subscriber.id, 'wrong-token']
            )
        )
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'The was an error please contact admin' in str(msg)
            for msg in messages
        ))


class PrivacyTests(TestCase):
    def test_newsletter_view(self):
        """
        Testing the privacy statement view.
        """
        self.client = Client()
        self.url = reverse('privacy')
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'support/support.html')
        self.assertEqual(response.context['title'], 'Privacy Statement')


class ReturnsTests(TestCase):
    def test_newsletter_view(self):
        """
        Testing the returns policy view.
        """
        self.client = Client()
        self.url = reverse('returns')
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'support/support.html')
        self.assertEqual(response.context['title'], 'Returns Policy')


class TermsTests(TestCase):
    def test_newsletter_view(self):
        """
        Testing the terms and conditions view.
        """
        self.client = Client()
        self.url = reverse('terms')
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'support/support.html')
        self.assertEqual(response.context['title'], 'Terms and Conditions')
