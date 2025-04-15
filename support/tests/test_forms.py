from django.test import TestCase
from unittest.mock import patch

from support.models import FaqsTopics

from ..forms import (
    ContactForm,
    ContactReplyForm,
    FaqsTopicsForm,
    FaqsForm,
    NewsletterForm,
    SubscriberForm
)


class ContactFormTests(TestCase):
    def setUp(self):
        """
        Create an instance of :form:`support.ContactForm` for tests.
        """
        self.form = ContactForm()

    def test_for_fields(self):
        """
        Check the :form:`support.ContactForm` instance has the expected fields.
        """
        expected_fields = [
            'name',
            'email',
            'message'
        ]

        # Assertions
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_placeholders(self):
        """
        Test for correct placeholders.
        """

        # Assertions
        self.assertEqual(
            self.form.fields['name'].widget.attrs.get('placeholder'),
            'Full Name *'
        )
        self.assertEqual(
            self.form.fields['email'].widget.attrs.get('placeholder'),
            'Email *'
        )
        self.assertEqual(
            self.form.fields['message'].widget.attrs.get('placeholder'),
            'Type your message here... *'
        )

    def test_for_custom_field_attributes(self):
        # Assertions
        self.assertEqual(
            self.form.fields['name'].widget.attrs.get('autofocus'),
            True
        )
        for field in self.form.fields.values():
            self.assertFalse(field.label)


class ContactReplyFormTests(TestCase):
    def setUp(self):
        """
        Create an instance of :form:`support.ContactReplyForm` for tests.
        """
        self.form = ContactReplyForm()

    def test_for_fields(self):
        """
        Check the :form:`support.ContactReplyForm` instance has the
        expected fields.
        """
        expected_fields = [
            'reply',
        ]

        # Assertions
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the reply field has the correct attributes.
        """
        # Assertions
        self.assertEqual(
            self.form.fields['reply'].widget.attrs.get('autofocus'),
            True
        )
        self.assertEqual(
            self.form.fields['reply'].widget.attrs.get('placeholder'),
            'Reply here...'
        )
        self.assertFalse(self.form.fields['reply'].label)


class FaqsTopicFormTests(TestCase):
    def setUp(self):
        """
        Create an instance of :form:`support.FaqsTopicsForm` for tests.
        """
        self.form = FaqsTopicsForm()

    def test_for_fields(self):
        """
        Check the :form:`support.FaqsTopicsForm` instance has the
        expected fields.
        """
        expected_fields = [
            'name',
        ]

        # Assertions
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the name field has the correct attributes.
        """
        # Assertions
        self.assertEqual(
            self.form.fields['name'].widget.attrs.get('placeholder'),
            'Topic name...'
        )
        self.assertFalse(self.form.fields['name'].label)


class FaqsFormTests(TestCase):
    def setUp(self):
        """
        Create instances of :model:`support.FaqsTopics` and
        :form:`support.FaqsForm` for tests.
        """
        # Create test topics
        self.topic_one = FaqsTopics.objects.create(name='Topic 1')
        self.topic_two = FaqsTopics.objects.create(name='Topic 2')
        # Creat test form
        self.form = FaqsForm()

    def test_for_fields(self):
        """
        Check the :form:`support.FaqsForm` instance has the expected fields.
        """
        expected_fields = [
            'topic',
            'question',
            'answer',
            'new_topic'
        ]

        # Assertions
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the form fields have the correct attributes.
        """
        # Assertions
        self.assertEqual(
            self.form.fields['question'].widget.attrs.get('placeholder'),
            'Question'
        )
        self.assertEqual(
            self.form.fields['answer'].widget.attrs.get('placeholder'),
            'Answer'
        )
        for field in self.form.fields.values():
            self.assertFalse(field.label)

    def test_topic_field_choices(self):
        """
        Confirm the topic choices include the add new topic options.
        """
        topic_choices = self.form.fields['topic'].choices
        expected_choices = [
            ('', '- Select a Topic -'),
            ('new', 'Add New Topic'),
            (1, 'Topic 1'),
            (2, 'Topic 2')
        ]

        # Assertions
        self.assertEqual(topic_choices, expected_choices)

    def test_save_method_with_new_topic(self):
        """
        Testing the save method with valid new topic data.
        """
        # Create form data.
        form_data = {
            'topic': 'new',
            'question': 'Test Question',
            'answer': 'Test Answer',
            'new_topic': 'New Topic'
            }
        form = FaqsForm(data=form_data)
        saved_instance = form.save(commit=True)

        # Assertions
        self.assertEqual(str(saved_instance.topic), 'New Topic')

    def test_save_method_with_invalid_new_topic(self):
        """
        Testing the save method error handling with patched `get_or_create`
        to simulate an exception.
        """
        # Create form data.
        form_data = {
            'topic': 'new',
            'question': 'Test Question',
            'answer': 'Test Answer',
            'new_topic': 'New Topic'
            }
        # Patch get_or_create to raise an exception
        with patch(
            'support.forms.FaqsTopics.objects.get_or_create',
            side_effect=Exception()
        ):
            form = FaqsForm(data=form_data)
            instance = form.save(commit=True)

            # Assertions for errors.
            self.assertIsNotNone(instance)
            self.assertIn('topic', form.errors)
            self.assertIn('An error occured:', form.errors['topic'][0])

    def test_clean_method_new_selected_blank_input(self):
        """
        Testing the clean method for new topic selection but blank input.
        """
        # Create form data.
        form_data = {
            'topic': 'new',
            'question': 'Test Question',
            'answer': 'Test Answer',
            'new_topic': '         '
            }
        # Create form.
        form = FaqsForm(data=form_data)

        # Assertions.
        self.assertFalse(form.is_valid())
        self.assertIn('topic', form.errors)
        self.assertIn('Topic cannot be blank.', form.errors['topic'][0])

    def test_clean_method_new_selected_exception_for_placeholder(self):
        """
        Testing the clean method error handling for new topic selection by
        patching the `first()` method to simulate an exception when getting
        a placeholder topic.
        """
        # Create form data.
        form_data = {
            'topic': 'new',
            'question': 'Test Question',
            'answer': 'Test Answer',
            'new_topic': 'New Topic'
        }
        # Patch first() to raise an exception
        with patch(
            'support.forms.FaqsTopics.objects.first',
            side_effect=Exception()
        ):
            # Create form.
            form = FaqsForm(data=form_data)

            # Assertions
            self.assertFalse(form.is_valid())
            self.assertIn('topic', form.errors)
            self.assertIn(
                'An error occured while processing the new topic:',
                form.errors['topic'][0]
            )

    def test_clean_method_with_existing_topic(self):
        """
        Testing the clean method with valid existing topic selected.
        """
        # Create form data.
        form_data = {
            'topic': '1',
            'question': 'Test Question',
            'answer': 'Test Answer',
            }
        form = FaqsForm(data=form_data)
        saved_instance = form.save(commit=True)

        # Assertions
        self.assertEqual(str(saved_instance.topic), 'Topic 1')

    def test_clean_method_exception_for_existing_topic(self):
        """
        Testing the clean method error handling for choosing an existing topic
        by patching the `get()` method when assigning the topic to simulate an
        exception.
        """
        # Create form data.
        form_data = {
            'topic': '1',
            'question': 'Test Question',
            'answer': 'Test Answer',
            }
        # Patch get() to raise an exception
        with patch(
            'support.forms.FaqsTopics.objects.get',
            side_effect=FaqsTopics.DoesNotExist()
        ):
            # Create form.
            form = FaqsForm(data=form_data)

            # Assertions
            self.assertFalse(form.is_valid())
            self.assertIn('topic', form.errors)
            self.assertIn(
                'Invalid topic selected.',
                form.errors['topic'][0]
            )


class NewsletterFormTests(TestCase):
    def setUp(self):
        """
        Create an instance of :form:`support.NewsletterForm` for tests.
        """
        # Create test form
        self.form = NewsletterForm()

    def test_for_fields(self):
        """
        Check the :form:`support.NewsletterForm` instance has the
        expected fields.
        """
        expected_fields = [
            'subject',
            'news_body'
        ]

        # Assertions
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the form fields have the correct attributes.
        """
        # Assertions
        self.assertEqual(
            self.form.fields['subject'].widget.attrs.get('placeholder'),
            'Subject'
        )
        self.assertEqual(
            self.form.fields['news_body'].widget.attrs.get('placeholder'),
            '...'
        )
        for field in self.form.fields.values():
            self.assertFalse(field.label)


class SubscriberFormTests(TestCase):
    def setUp(self):
        """
        Create an existing email and instance of :form:`support.SubscriberForm`
        for tests.
        """
        self.existing_email = 'already@here.com'
        self.form = SubscriberForm()

    def test_for_fields(self):
        """
        Check the :form:`support.SubscriberForm` instance has the
        expected fields.
        """
        expected_fields = [
            'email'
        ]

        # Assertions
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the form fields have the correct attributes.
        """
        # Assertions
        self.assertEqual(
            self.form.fields['email'].widget.attrs.get('placeholder'),
            'email@example.com'
        )
        for field in self.form.fields.values():
            self.assertFalse(field.label)

    def test_existing_email_does_not_raise_error(self):
        """
        Test that entering an email that already exists passes on unique
        exceptions to let the view handle it.
        """
        form_data = {'email': 'already@here.com'}
        form = SubscriberForm(data=form_data)

        # Assertions
        self.assertTrue(form.is_valid())
        self.assertNotIn('email', form.errors)
