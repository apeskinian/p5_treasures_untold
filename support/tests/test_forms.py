from django.test import TestCase
from unittest.mock import patch

from ..forms import (
    ContactForm, ContactReplyForm,
    FaqsTopicsForm, FaqsForm, NewsletterForm, SubscriberForm
)
from support.models import FaqsTopics


class ContactFormTests(TestCase):
    def setUp(self):
        """
        Create test form.
        """
        self.form = ContactForm()

    def test_for_fields(self):
        """
        Check the form has the expected fields.
        """
        expected_fields = [
            'name',
            'email',
            'message'
        ]
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_placeholders(self):
        """
        Test for correct placeholders.
        """
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
        self.assertEqual(
            self.form.fields['name'].widget.attrs.get('autofocus'),
            True
        )
        for field in self.form.fields.values():
            self.assertFalse(field.label)


class ContactReplyFormTests(TestCase):
    def setUp(self):
        """
        Create form.
        """
        self.form = ContactReplyForm()

    def test_for_fields(self):
        """
        Check the form has the expected fields.
        """
        expected_fields = [
            'reply',
        ]
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the reply field has the correct attributes.
        """
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
        Create form.
        """
        self.form = FaqsTopicsForm()

    def test_for_fields(self):
        """
        Check the form has the expected fields.
        """
        expected_fields = [
            'name',
        ]
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the name field has the correct attributes.
        """
        self.assertEqual(
            self.form.fields['name'].widget.attrs.get('placeholder'),
            'Topic name...'
        )
        self.assertFalse(self.form.fields['name'].label)


class FaqsFormTests(TestCase):
    def setUp(self):
        """
        Create form.
        """
        # Create test topics
        self.topic_one = FaqsTopics.objects.create(name='Topic 1')
        self.topic_two = FaqsTopics.objects.create(name='Topic 2')
        # Creat test form
        self.form = FaqsForm()

    def test_for_fields(self):
        """
        Check the form has the expected fields.
        """
        expected_fields = [
            'topic',
            'question',
            'answer',
            'new_topic'
        ]
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the form fields have the correct attributes.
        """
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
        # Assertion
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
        # Assertion for form validation.
        self.assertTrue(form.is_valid())
        # Save the form.
        saved_instance = form.save(commit=True)
        # Assertion for name replacement.
        self.assertEqual(str(saved_instance.topic), 'New Topic')

    def test_save_method_with_invalid_new_topic(self):
        """
        Testing the save method with patched exception.
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
            # Create form and assert validity.
            form = FaqsForm(data=form_data)
            self.assertTrue(form.is_valid())
            instance = form.save(commit=True)
            self.assertIsNotNone(instance)

            # Assertions for errors.
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
        Testing the clean method for new topic selection exception
        handling.
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

            # Assertions for errors.
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
        # Assertion for form validation.
        self.assertTrue(form.is_valid())
        # Save the form.
        saved_instance = form.save(commit=True)
        # Assertion for name replacement.
        self.assertEqual(str(saved_instance.topic), 'Topic 1')

    def test_clean_method_exception_for_existing_topic(self):
        """
        Testing the clean method for choosing an existing topic exception
        handling.
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

            # Assertions for errors.
            self.assertFalse(form.is_valid())
            self.assertIn('topic', form.errors)
            self.assertIn(
                'Invalid topic selected.',
                form.errors['topic'][0]
            )


class NewsletterFormTests(TestCase):
    def setUp(self):
        """
        Create form.
        """
        # Create test form
        self.form = NewsletterForm()

    def test_for_fields(self):
        """
        Check the form has the expected fields.
        """
        expected_fields = [
            'subject',
            'news_body'
        ]
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the form fields have the correct attributes.
        """
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
        Create form.
        """
        # Create existing email
        self.existing_email = 'already@here.com'
        # Create test form
        self.form = SubscriberForm()

    def test_for_fields(self):
        """
        Check the form has the expected fields.
        """
        expected_fields = [
            'email'
        ]
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_for_field_attributes(self):
        """
        Check the form fields have the correct attributes.
        """
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

        self.assertTrue(form.is_valid())
        self.assertNotIn('email', form.errors)
