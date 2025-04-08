from django.contrib.auth.models import User
from django.test import TestCase

from ..forms import UserProfileForm
from profiles.models import UserProfile


class ProfileFormTests(TestCase):
    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='test',
            email='tesstyuza@test.com',
            password='password123',
        )
        self.user_profile, created = (
            UserProfile.objects.get_or_create(user=self.user)
        )

        self.form = UserProfileForm(instance=self.user_profile)

    def test_form_fields(self):
        """
        Test the form includes the expected fields.
        """
        expected_fields = [
            'default_full_name',
            'default_phone_number',
            'default_street_address_1',
            'default_street_address_2',
            'default_town_city',
            'default_postcode',
            'default_county',
            'default_country',
            'email'
        ]
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_placeholders(self):
        """
        Test to check placeholders are correct and autofocus is set to the
        `default_full_name` field.
        """
        self.assertEqual(
            self.form.fields['default_full_name']
            .widget.attrs.get('placeholder'),
            'Full Name'
        )
        self.assertEqual(
            self.form.fields['default_phone_number']
            .widget.attrs.get('placeholder'),
            'Phone Number'
        )
        self.assertEqual(
            self.form.fields['default_street_address_1']
            .widget.attrs.get('placeholder'),
            'Street Address 1'
        )
        self.assertEqual(
            self.form.fields['default_street_address_2']
            .widget.attrs.get('placeholder'),
            'Street Address 2'
        )
        self.assertEqual(
            self.form.fields['default_town_city']
            .widget.attrs.get('placeholder'),
            'Town or City'
        )
        self.assertEqual(
            self.form.fields['default_postcode']
            .widget.attrs.get('placeholder'),
            'Postal Code'
        )
        self.assertEqual(
            self.form.fields['default_county']
            .widget.attrs.get('placeholder'),
            'County, State or Locality'
        )

    def test_labels_are_removed(self):
        """
        All labels should be removed (set to False).
        """
        for field in self.form.fields.values():
            self.assertFalse(field.label)

    def test_aria_label_attributes(self):
        """
        Test that custom aria-labels are set.
        """
        country_attrs = self.form.fields['default_country'].widget.attrs
        self.assertEqual(country_attrs.get('aria-label'), 'country')

        email_attrs = self.form.fields['email'].widget.attrs
        self.assertEqual(email_attrs.get('aria-label'), 'email')
