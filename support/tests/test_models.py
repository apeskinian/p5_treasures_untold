import re

from django.test import TestCase

from ..models import ContactMessage, Faqs, FaqsTopics, Newsletter, Subscriber


class ContactMessageTests(TestCase):
    def setUp(self):
        """
        Create instance of :model:`support.ContactMessage` for tests.
        """
        self.message = ContactMessage.objects.create(
            name='Tess Tyuza',
            email='tess@tyuza.com',
            message='Test'
        )

    def test_ticket_number_generator(self):
        """
        Tests the ticket number matches the correct format.
        """
        message = self.message
        ticket = message._generate_ticket_number()

        # Assertions
        self.assertTrue(re.match(r'^TU-[A-F0-9]{8}$', ticket))

    def test_return_string(self):
        """
        Test the return string is correct.
        """
        # Assertions
        self.assertEqual(
            str(self.message),
            f'{self.message.ticket_number} - {self.message.name}'
        )


class FaqsTests(TestCase):
    def setUp(self):
        """
        Create instances of :model:`support.FaqsTopics` and
        :model:`support.Faqs` for tests.
        """
        self.topic = FaqsTopics.objects.create(name='Topic')
        self.faq = Faqs.objects.create(
            topic=self.topic,
            question='Question',
            answer='Answer'
        )

    def test_return_string(self):
        """
        Test the return string is correct.
        """
        # Assertions
        self.assertEqual(str(self.faq), self.faq.question)


class NewsletterTests(TestCase):
    def setUp(self):
        """
        Create instance of :model:`support.Newsletter` for tests.
        """
        self.newsletter = Newsletter.objects.create(
            subject='Subject',
            news_body='News'
        )

    def test_return_string(self):
        """
        Test the return string is correct.
        """

        # Assertions
        self.assertEqual(str(self.newsletter), self.newsletter.subject)


class SubscriberTests(TestCase):
    def setUp(self):
        """
        Create instance of :model:`support.Subscriber` for tests.
        """
        self.subscriber = Subscriber.objects.create(
            email='tess@tyuza.com'
        )

    def test_return_string(self):
        """
        Test the return string is correct.
        """

        # Assertions
        self.assertEqual(str(self.subscriber), self.subscriber.email)
