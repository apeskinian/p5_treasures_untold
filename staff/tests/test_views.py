from datetime import timedelta

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.messages import get_messages
from unittest.mock import patch, MagicMock

from products.models import Product, Realm
from products.forms import ProductForm, RealmForm
from support.models import (
    Faqs, FaqsTopics, ContactMessage, Newsletter, Subscriber
)
from support.forms import (
    FaqsForm, FaqsTopicsForm, ContactReplyForm, NewsletterForm
)


class DashboardTests(TestCase):
    def setUp(self):
        """
        Create staff user for tests and log in.
        """
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        self.staff_user.save()
        self.client.login(username='staffuser', password='password')

    def test_dashboard_view(self):
        """
        Test the dashbooard view.
        """
        self.url = reverse('dashboard')
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['title'], 'Staff Dashboard')


class FaqAdminTests(TestCase):
    def setUp(self):
        """
        Create staff user for tests and log in. Also create intances of
        :model:`support.Faqs` and :model:`support.FaqsTopics` for testing.
        """
        # Creating staff user and logging in.
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        self.staff_user.save()
        self.client.login(username='staffuser', password='password')
        # Creating test FAQs
        self.faq_topic = FaqsTopics.objects.create(
            id=1,
            name='Test Topic'
        )
        self.test_faq = Faqs.objects.create(
            id=1,
            topic=self.faq_topic,
            question='Is this a FAQ?',
            answer='Why yes, yes it is.'
        )

    def test_get_add_faq_form(self):
        """
        Test that the dashboard displays the FAQ tab and context includes a
        blank instance of :form:`support.FaqsForm`.
        """
        self.url = reverse('manage_faq')
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'FAQ')
        self.assertIsInstance(response.context['form'], FaqsForm)

    def test_get_edit_faq_form(self):
        """
        Test that the dashboard displays the FAQ tab and context includes an
        instance of :form:`support.FaqsForm` pre-filled with the selected
        :model:`support.Faq`.
        """
        self.url = reverse('manage_faq', args=[self.test_faq.id])
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'FAQ')
        self.assertIsInstance(response.context['form'], FaqsForm)
        self.assertEqual(response.context['form'].instance, self.test_faq)

    def test_get_delete_faq_confirmation(self):
        """
        Test that the dashboard displays the FAQ tab and context includes the
        instance of :model:`support.Faq` sent as an argument.
        """
        self.url = reverse('manage_faq', args=['delete', self.test_faq.id])
        response = self.client.get(self.url)

        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'FAQ')
        self.assertEqual(response.context['to_delete'], self.test_faq)

    def test_post_add_faq_form(self):
        """
        Test the creation of a new instance of :model:`support.Faq`.
        """
        self.url = reverse('manage_faq')
        response = self.client.post(
            self.url,
            {
                'topic': self.faq_topic.id,
                'question': 'New Question',
                'answer': 'New Answer'
            }
        )
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'FAQ Added' in str(msg)
            for msg in messages
        ))
        self.assertTrue(Faqs.objects.filter(question='New Question').exists())

    def test_post_edit_faq_form(self):
        """
        Test the successful update of a :model:`support.Faq` instance.
        """
        self.url = reverse('manage_faq', args=[self.test_faq.id])
        response = self.client.post(
            self.url,
            {
                'topic': self.faq_topic.id,
                'question': 'Updated Question',
                'answer': 'Why yes, yes it is.'
            }
        )
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'FAQ updated' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            Faqs.objects.filter(question='Is this a FAQ?').exists()
            )
        self.assertTrue(
            Faqs.objects.filter(question='Updated Question').exists()
            )

    def test_post_edit_faq_form_invalid(self):
        """
        Test the error handling when attempting to update a
        :model:`support.Faq` instance with an invalid form.
        """
        self.url = reverse('manage_faq', args=[self.test_faq.id])
        response = self.client.post(
            self.url,
            {
                'topic': self.test_faq.id,
                'question': 'Updated Question',
                'answer': ''
            }
        )
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'Failed to update FAQ' in str(msg)
            for msg in messages
        ))

    def test_post_delete_faq(self):
        """
        Test the deletion of a :model:`support.Faq` instance.
        """
        self.url = reverse('manage_faq', args=['delete', self.test_faq.id])
        response = self.client.post(self.url)

        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'FAQ deleted' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            Faqs.objects.filter(question='Is this a FAQ?').exists()
            )

    def test_post_delete_faq_error(self):
        """
        Test the error handling of a simulated error when attempting to delete
        a :model:`support.Faq` instance.
        """
        self.url = reverse('manage_faq', args=['delete', self.test_faq.id])
        with patch.object(Faqs, 'delete', side_effect=Exception()):
            response = self.client.post(self.url)
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertTrue(any(
            'Error deleting FAQ' in str(msg)
            for msg in messages
        ))

    def test_get_add_faqtopic_form(self):
        """
        Testing for dashboard to be showing the faqs tab and a new form for
        adding a faq topic to be in the context.
        """
        self.url = reverse('manage_faq_topic')
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'FAQ Topic')
        self.assertIsInstance(response.context['form'], FaqsTopicsForm)

    def test_get_edit_faqtopic_form(self):
        """
        Testing for dashboard to be showing the faqs tab and a form for
        editing a faq topic to be in the context.
        """
        self.url = reverse('manage_faq_topic', args=[self.faq_topic.id])
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'FAQ Topic')
        self.assertIsInstance(response.context['form'], FaqsTopicsForm)
        self.assertEqual(response.context['form'].instance, self.faq_topic)

    def test_get_delete_faqtopic_confirmation(self):
        """
        Testing for dashboard to be showing the faqs tab and the same instance
        of `faq_topic` in the context that was sent as an argument for
        deletion.
        """
        self.url = reverse(
            'manage_faq_topic', args=['delete', self.faq_topic.id]
        )
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'FAQ Topic')
        self.assertEqual(response.context['to_delete'], self.faq_topic)

    def test_post_add_faqtopic_form(self):
        """
        Test the addition of a new faq topic.
        """
        self.url = reverse('manage_faq_topic')
        response = self.client.post(
            self.url,
            {
                'name': 'New Topic',
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'FAQ topic Added' in str(msg)
            for msg in messages
        ))
        self.assertTrue(
            FaqsTopics.objects.filter(name='New Topic').exists()
        )

    def test_post_edit_faqtopic_form(self):
        """
        Test the update of an existing faq topic.
        """
        self.url = reverse('manage_faq_topic', args=[self.faq_topic.id])
        response = self.client.post(
            self.url,
            {
                'name': 'New New Topic',
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'FAQ topic updated' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            FaqsTopics.objects.filter(name='Test Topic').exists()
            )
        self.assertTrue(
            FaqsTopics.objects.filter(name='New New Topic').exists()
            )

    def test_post_edit_faqtopic_form_invalid(self):
        """
        Test the error handling of update of an existing faq topic.
        """
        self.url = reverse('manage_faq_topic', args=[self.faq_topic.id])
        response = self.client.post(
            self.url,
            {
                'name': ''
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Failed to update FAQ topic' in str(msg)
            for msg in messages
        ))

    def test_post_delete_faqtopic(self):
        """
        Test the deletion of an existing faq topic.
        """
        self.url = reverse(
            'manage_faq_topic', args=['delete', self.faq_topic.id]
        )
        response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'FAQ topic deleted' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            FaqsTopics.objects.filter(name='Test Topic').exists()
            )

    def test_post_delete_faqtopic_error(self):
        """
        Test the error handling of deletion of an existing faq topic.
        """
        self.url = reverse(
            'manage_faq_topic', args=['delete', self.faq_topic.id]
        )

        with patch.object(FaqsTopics, 'delete', side_effect=Exception()):
            response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Error deleting FAQ topic' in str(msg)
            for msg in messages
        ))


class ProductAdminTests(TestCase):
    def setUp(self):
        """
        Create staff user and url for tests.
        """
        # Creating staff user and logging in.
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        self.staff_user.save()
        self.client.login(username='staffuser', password='password')
        # Create test products and realms
        self.test_realm = Realm.objects.create(name='test_realm')
        self.test_product = Product.objects.create(
            id=1,
            name='test product',
            realm=self.test_realm,
            description='product descripton',
            price=10.00,
            stock=5,
        )

    def test_get_add_product_form(self):
        """
        Testing for dashboard to be showing the products tab and a new form for
        adding a product to be in the context.
        """
        self.url = reverse('manage_product')
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Product')
        self.assertIsInstance(response.context['form'], ProductForm)

    def test_get_edit_product_form(self):
        """
        Testing for dashboard to be showing the products tab and a form for
        editing a product to be in the context.
        """
        self.url = reverse('manage_product', args=[self.test_product.id])
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Product')
        self.assertIsInstance(response.context['form'], ProductForm)
        self.assertEqual(response.context['form'].instance, self.test_product)

    def test_get_delete_product_confirmation(self):
        """
        Testing for dashboard to be showing the product tab and the same
        instance of `product` in the context that was sent as an argument for
        deletion.
        """
        self.url = reverse(
            'manage_product', args=['delete', self.test_product.id]
        )
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Product')
        self.assertEqual(response.context['to_delete'], self.test_product)

    def test_post_add_product_form(self):
        """
        Test the addition of a new product.
        """
        self.url = reverse('manage_product')
        response = self.client.post(
            self.url,
            {
                'name': 'test new product',
                'realm': self.test_realm.id,
                'description': 'product descripton',
                'price': 20.00,
                'stock': 5,
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Product Added' in str(msg)
            for msg in messages
        ))
        self.assertTrue(
            Product.objects.filter(name='test new product').exists()
        )

    def test_post_edit_product_form(self):
        """
        Test the update of an existing product.
        """
        self.url = reverse('manage_product', args=[self.test_product.id])
        response = self.client.post(
            self.url,
            {
                'name': 'Updated Product',
                'realm': self.test_realm.id,
                'description': 'product descripton',
                'price': 20.00,
                'stock': 5,
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Product updated' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            Product.objects.filter(name='test product').exists()
            )
        self.assertTrue(
            Product.objects.filter(name='Updated Product').exists()
            )

    def test_post_edit_product_form_invalid(self):
        """
        Test the error handling of update of an existing product.
        """
        self.url = reverse('manage_product', args=[self.test_product.id])
        response = self.client.post(
            self.url,
            {
                'name': '',
                'realm': self.test_realm.id,
                'description': 'product descripton',
                'price': 20.00,
                'stock': 5,
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Failed to update product' in str(msg)
            for msg in messages
        ))

    def test_post_delete_product(self):
        """
        Test the deletion of an existing product.
        """
        self.url = reverse(
            'manage_product', args=['delete', self.test_product.id]
            )
        response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Product deleted' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            Product.objects.filter(name='test product').exists()
            )

    def test_post_delete_product_error(self):
        """
        Test the error handling of deletion of an existing product.
        """
        self.url = reverse(
            'manage_product', args=['delete', self.test_product.id]
        )

        with patch.object(Product, 'delete', side_effect=Exception()):
            response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Error deleting product' in str(msg)
            for msg in messages
        ))


class RealmAdminTests(TestCase):
    def setUp(self):
        """
        Create staff user and url for tests.
        """
        # Creating staff user and logging in.
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        self.staff_user.save()
        self.client.login(username='staffuser', password='password')
        # Create test realm
        self.test_realm = Realm.objects.create(name='test_realm')

    def test_get_add_realm_form(self):
        """
        Testing for dashboard to be showing the products tab and a new form for
        adding a realm to be in the context.
        """
        self.url = reverse('manage_realm')
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Realm')
        self.assertIsInstance(response.context['form'], RealmForm)

    def test_get_edit_realm_form(self):
        """
        Testing for dashboard to be showing the products tab and a form for
        editing a realm to be in the context.
        """
        self.url = reverse('manage_realm', args=[self.test_realm.id])
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Realm')
        self.assertIsInstance(response.context['form'], RealmForm)
        self.assertEqual(response.context['form'].instance, self.test_realm)

    def test_get_delete_realm_confirmation(self):
        """
        Testing for dashboard to be showing the product tab and the same
        instance of `realm` in the context that was sent as an argument for
        deletion.
        """
        self.url = reverse(
            'manage_realm', args=['delete', self.test_realm.id]
        )
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Realm')
        self.assertEqual(response.context['to_delete'], self.test_realm)

    def test_post_add_realm_form(self):
        """
        Test the addition of a new realm.
        """
        self.url = reverse('manage_realm')
        response = self.client.post(
            self.url,
            {
                'name': 'test_new_realm',
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Realm created' in str(msg)
            for msg in messages
        ))
        self.assertTrue(
            Realm.objects.filter(name='test_new_realm').exists()
        )

    def test_post_edit_realm_form(self):
        """
        Test the update of an existing realm.
        """
        self.url = reverse('manage_realm', args=[self.test_realm.id])
        response = self.client.post(
            self.url,
            {
                'name': 'Updated_Realm',
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Realm updated' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            Realm.objects.filter(name='test_realm').exists()
            )
        self.assertTrue(
            Realm.objects.filter(name='Updated_Realm').exists()
            )

    def test_post_edit_realm_form_invalid(self):
        """
        Test the error handling of update of an existing realm.
        """
        self.url = reverse('manage_realm', args=[self.test_realm.id])
        response = self.client.post(
            self.url,
            {
                'name': '',
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Failed to update realm' in str(msg)
            for msg in messages
        ))

    def test_post_delete_realm(self):
        """
        Test the deletion of an existing realm.
        """
        self.url = reverse(
            'manage_realm', args=['delete', self.test_realm.id]
            )
        response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Realm deleted' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            Realm.objects.filter(name='test_realm').exists()
            )

    def test_post_delete_realm_error(self):
        """
        Test the error handling of deletion of an existing realm.
        """
        self.url = reverse(
            'manage_realm', args=['delete', self.test_realm.id]
        )

        with patch.object(Realm, 'delete', side_effect=Exception()):
            response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Error deleting realm' in str(msg)
            for msg in messages
        ))


class ManageMessageTests(TestCase):
    def setUp(self):
        """
        Create staff user and url for tests.
        """
        # Creating staff user and logging in.
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        self.staff_user.save()
        self.client.login(username='staffuser', password='password')
        # Create test message
        self.test_message = ContactMessage.objects.create(
            id=1,
            ticket_number='test1234',
            name='Tess Tyuza',
            email='tess@tyuza.com',
            message='this is a test message'
        )

    def test_get_send_message_reply_form(self):
        """
        Testing for dashboard to be showing the messages tab and a new form for
        sending a reply to a message to be in the context.
        """
        self.url = reverse('manage_message', args=[self.test_message.id])
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Message')
        self.assertIsInstance(response.context['form'], ContactReplyForm)
        self.assertEqual(response.context['form'].instance, self.test_message)

    def test_get_delete_message_confirmation(self):
        """
        Testing for dashboard to be showing the messages tab and the same
        instance of `ContactMessage` in the context that was sent as an
        argument for deletion.
        """
        self.url = reverse(
            'manage_message', args=[self.test_message.id, 'delete']
        )
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Message')
        self.assertEqual(response.context['to_delete'], self.test_message)

    def test_post_delete_message(self):
        """
        Test the deletion of an existing message.
        """
        self.url = reverse(
            'manage_message', args=[self.test_message.id, 'delete']
        )
        response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Message deleted' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            ContactMessage.objects.filter(ticket_number='test1234').exists()
            )

    def test_post_delete_message_error(self):
        """
        Test the error handling of deletion of an existing message.
        """
        self.url = reverse(
            'manage_message', args=[self.test_message.id, 'delete']
        )

        with patch.object(ContactMessage, 'delete', side_effect=Exception()):
            response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Error deleting message' in str(msg)
            for msg in messages
        ))

    def test_post_message_reply_with_invalid_form(self):
        """
        Test the error handling of replying to a message.
        """
        self.url = reverse('manage_message', args=[self.test_message.id])
        response = self.client.post(
            self.url,
            {
                'reply': '  ',
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Failed to send reply' in str(msg)
            for msg in messages
        ))

    @patch('staff.views.send_mail')
    def test_post_message_reply(self, mock_send_mail):
        """
        Test the reply to a message with a valid reply form.
        """
        mock_request = MagicMock()
        mock_request.build_absolute_uri.return_value = 'http://example.com'

        self.url = reverse('manage_message', args=[self.test_message.id])
        response = self.client.post(
            self.url,
            {
                'reply': 'This is a test for a valid reply.',
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Reply sent' in str(msg)
            for msg in messages
        ))
        mock_send_mail.assert_called_once()


class ManageNewslettersTests(TestCase):
    def setUp(self):
        """
        Create staff user and model instances for tests.
        """
        # Creating staff user and logging in.
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        self.staff_user.save()
        self.client.login(username='staffuser', password='password')
        # Create newsletter.
        self.existing_newsletter = Newsletter.objects.create(
            subject='Test Newsletter',
            news_body='Test newsletter content.'
        )
        # Create active subscriber to receive newsletter.
        self.subscriber_active = Subscriber.objects.create(
            email='tess@tyuza.com',
            is_active=True,
            date_joined=timezone.localdate(),
            token='test_token'
        )

    def test_get_create_newsletter_form(self):
        """
        Testing for dashboard to be showing the newsletter tab and a new form
        for creating a newsletter to be in the context.
        """
        self.url = reverse('manage_newsletters')
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Newsletter')
        self.assertIsInstance(response.context['form'], NewsletterForm)

    def test_get_view_newsletter(self):
        """
        Testing for dashboard to be showing the newsletter tab and the same
        instance of `Newsletter` in the context that was sent as an argument.
        """
        self.url = reverse(
            'manage_newsletters', args=[self.existing_newsletter.id]
        )
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Newsletter')
        self.assertIsInstance(response.context['form'], NewsletterForm)
        self.assertEqual(
            response.context['form'].instance, self.existing_newsletter
        )

    def test_get_delete_newsletter_confirmation(self):
        """
        Testing for dashboard to be showing the newsletter tab and the same
        instance of `Newsletter` in the context that was sent as an argument.
        """
        self.url = reverse(
            'manage_newsletters', args=['delete', self.existing_newsletter.id]
        )
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Newsletter')
        self.assertEqual(
            response.context['to_delete'], self.existing_newsletter
        )

    def test_post_delete_newsletter(self):
        """
        Test the deletion of an existing newsletter.
        """
        self.url = reverse(
            'manage_newsletters', args=['delete', self.existing_newsletter.id]
            )
        response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Newsletter deleted' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            Newsletter.objects.filter(subject='Test Newsletter').exists()
            )

    def test_post_delete_newsletter_error(self):
        """
        Test the error handling of deletion of an existing newsletter.
        """
        self.url = reverse(
            'manage_newsletters', args=['delete', self.existing_newsletter.id]
        )

        with patch.object(Newsletter, 'delete', side_effect=Exception()):
            response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Error deleting newsletter' in str(msg)
            for msg in messages
        ))

    def test_post_send_newsletter_with_invalid_form(self):
        """
        Test the error handling of sending a newsletter.
        """
        self.url = reverse('manage_newsletters')
        response = self.client.post(
            self.url,
            {
                'subject': 'Newsletter with no content',
                'news_body': '    '
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Failed to create newsletter' in str(msg)
            for msg in messages
        ))

    @patch('staff.views.send_mail')
    def test_post_newsletter_creation(self, mock_send_mail):
        """
        Test the creation and sending of a newsletter.
        """
        mock_request = MagicMock()
        mock_request.build_absolute_uri.return_value = 'http://example.com'

        self.url = reverse('manage_newsletters')
        response = self.client.post(
            self.url,
            {
                'subject': 'Newsletter with content',
                'news_body': 'Some great news!'
            }
        )
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Newsletter created' in str(msg)
            for msg in messages
        ))
        self.assertTrue(any(
            'Newsletter sent to all subscribers' in str(msg)
            for msg in messages
        ))
        mock_send_mail.assert_called_once()


class ManageSubscriberTests(TestCase):
    def setUp(self):
        """
        Create staff user and model instances for tests.
        """
        # Creating staff user and logging in.
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        self.staff_user.save()
        self.client.login(username='staffuser', password='password')
        # Create newsletter.
        self.existing_newsletter = Newsletter.objects.create(
            subject='Test Newsletter',
            news_body='Test newsletter content.'
        )
        # Create active subscriber to receive newsletter.
        self.subscriber = Subscriber.objects.create(
            id=1,
            email='tess@tyuza.com'
        )

    def test_get_delete_subscriber_confirmation(self):
        """
        Testing for dashboard to be showing the newsletter tab and the same
        instance of `Subscriber` in the context that was sent as an argument.
        """
        self.url = reverse(
            'manage_subscriber', args=[self.subscriber.id]
        )
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Newsletter')
        self.assertEqual(response.context['to_delete'], self.subscriber)

    def test_post_delete_subscriber_error(self):
        """
        Test the error handling of deletion of an existing subscriber.
        """
        self.url = reverse(
            'manage_subscriber', args=[self.subscriber.id]
        )

        with patch.object(Subscriber, 'delete', side_effect=Exception()):
            response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Error unsubscribing' in str(msg)
            for msg in messages
        ))

    def test_post_delete_subscriber(self):
        """
        Test the deletion of an existing subscriber.
        """
        self.url = reverse('manage_subscriber', args=[self.subscriber.id])
        response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Unsubscribed' in str(msg)
            for msg in messages
        ))
        self.assertFalse(
            Subscriber.objects.filter(email='tess@tyuza.com').exists()
            )


class ManageExpiredSubscriberTests(TestCase):
    def setUp(self):
        """
        Create staff user and model instances for tests.
        """
        # Creating staff user and logging in.
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        self.staff_user.save()
        self.client.login(username='staffuser', password='password')
        # Create newsletter.
        self.existing_newsletter = Newsletter.objects.create(
            subject='Test Newsletter',
            news_body='Test newsletter content.'
        )
        # Create expired subscriber
        self.expired_subscriber = Subscriber.objects.create(
            id=1,
            email='expireds@tyuza.com',
            token='test_token1',
            token_created_at=timezone.now() - timedelta(days=400)
        )
        # Create active subscriber
        self.active_subscriber = Subscriber.objects.create(
            id=2,
            email='active@tyuza.com',
            is_active=True,
            token='test_token2',
        )
        # Create a pending subscriber
        self.pending_subscriber = Subscriber.objects.create(
            id=3,
            email='pending@tyuza.com',
            token='test_token3',
            token_created_at=timezone.now()
        )

    def test_get_delete_expired_subscribers_confirmation(self):
        """
        Testing for dashboard to be showing the newsletter tab and the instance
        of each `Subscribe` to be in the relevant context.
        """
        self.url = reverse(
            'clear_expired_subscribers'
        )
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertEqual(response.context['active_tab'], 'Newsletter')
        self.assertIn(
            self.expired_subscriber, response.context['expired_subscribers']
        )
        self.assertIn(
            self.active_subscriber, response.context['active_subscribers']
        )
        self.assertIn(
            self.pending_subscriber,
            response.context['unconfirmed_subscribers']
        )

    def test_post_delete_expired_subscribers_error(self):
        """
        Test the error handling of deletion of an expired subscribers.
        """
        # Delete the expired subscriber so that none will be found.
        self.expired_subscriber.delete()
        # Make the request
        self.url = reverse('clear_expired_subscribers')
        response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'There are no expired subscribers' in str(msg)
            for msg in messages
        ))
        self.assertIn(self.pending_subscriber, Subscriber.objects.all())
        self.assertIn(self.active_subscriber, Subscriber.objects.all())

    def test_post_delete_expired_subscribers(self):
        """
        Test the error handling of deletion of an expired subscribers.
        """
        # Make the request
        self.url = reverse('clear_expired_subscribers')
        response = self.client.post(self.url)
        # Assertions
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'All expired subscribers removed' in str(msg)
            for msg in messages
        ))
        self.assertIn(self.pending_subscriber, Subscriber.objects.all())
        self.assertIn(self.active_subscriber, Subscriber.objects.all())
        self.assertNotIn(self.expired_subscriber, Subscriber.objects.all())


class CancelActionTests(TestCase):
    def setUp(self):
        """
        Create staff user and model instances for tests.
        """
        # Creating staff user and logging in.
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        self.staff_user.save()
        self.client.login(username='staffuser', password='password')

    def test_faq_action_cancelled(self):
        """
        Test message sent to user on cancellation of a FAQ based action.
        """
        return_url = reverse('manage_faq')
        url = reverse('cancel_action', args=['Delete', 'FAQ', return_url])
        response = self.client.get(url)
        messages = list(get_messages(response.wsgi_request))
        # Assertions
        self.assertTrue(any(
            'Delete FAQ cancelled.' in str(msg)
            for msg in messages
        ))
        self.assertRedirects(response, return_url)

    def test_remove_subscriber_cancelled(self):
        """
        Test message sent to user on cancellation of a subscriber removal.
        """
        return_url = reverse('manage_newsletters')
        url = reverse(
            'cancel_action',
            args=['Remove', 'Newletter', return_url]
        )
        response = self.client.get(url)
        messages = list(get_messages(response.wsgi_request))
        # Assertions
        self.assertTrue(any(
            'Removing subscriber cancelled.' in str(msg)
            for msg in messages
        ))
        self.assertRedirects(response, return_url)

    def test_clearing_expired_subscribers_cancelled(self):
        """
        Test message sent to user on cancellation of a clearing expired
        subscribers.
        """
        return_url = reverse('manage_newsletters')
        url = reverse(
            'cancel_action',
            args=['Clear', 'Newletter', return_url]
        )
        response = self.client.get(url)
        messages = list(get_messages(response.wsgi_request))
        # Assertions
        self.assertTrue(any(
            'Clearing expired subscribers cancelled.' in str(msg)
            for msg in messages
        ))
        self.assertRedirects(response, return_url)

    def test_replying_to_message_cancelled(self):
        """
        Test message sent to user on cancellation of a replying to a contact
        message.
        """
        return_url = reverse('dashboard')
        url = reverse(
            'cancel_action',
            args=['Reply', 'Message', return_url]
        )
        response = self.client.get(url)
        messages = list(get_messages(response.wsgi_request))
        # Assertions
        self.assertTrue(any(
            'Reply to message cancelled.' in str(msg)
            for msg in messages
        ))
        self.assertRedirects(response, return_url)

    def test_viewing_newsletter_cancelled(self):
        """
        Test no message is sent when the action was 'View'.
        """
        return_url = reverse('manage_newsletters')
        url = reverse(
            'cancel_action',
            args=['View', 'Newsletter', return_url]
        )
        response = self.client.get(url)
        messages = list(get_messages(response.wsgi_request))

        # Assertions
        self.assertEqual(messages, [])
        self.assertRedirects(response, return_url)
