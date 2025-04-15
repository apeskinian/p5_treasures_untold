from django.test import TestCase

from ..forms import OrderForm


class OrderFormTests(TestCase):
    def setUp(self):
        """
        Create instance of :form:`checkout.OrderForm` for tests.
        """
        self.form = OrderForm()

    def test_order_form_fields(self):
        """
        Test the instance of :form:`checkout.OrderForm` includes all the
        expected fields.
        """
        expected_fields = [
            'full_name',
            'email',
            'phone_number',
            'street_address_1',
            'street_address_2',
            'town_city',
            'county',
            'postcode',
            'country',
        ]

        # Assertions
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_placeholders_and_autofocus(self):
        """
        Test that the placeholders are correct and autofocus is set on
        the `full_name` field.
        """
        # Assertions
        self.assertEqual(
            self.form.fields['full_name'].widget.attrs.get('autofocus'), True
        )
        self.assertEqual(
            self.form.fields['full_name'].widget.attrs.get('placeholder'),
            'Full Name *'
        )
        self.assertEqual(
            self.form.fields['email'].widget.attrs.get('placeholder'),
            'Email *'
        )
        self.assertEqual(
            self.form.fields['phone_number'].widget.attrs.get('placeholder'),
            'Phone Number'
        )
        self.assertEqual(
            self.form.fields['street_address_1'].widget.attrs.get(
                'placeholder'
            ),
            'Street Address 1 *'
        )
        self.assertEqual(
            self.form.fields['street_address_2'].widget.attrs.get(
                'placeholder'
            ),
            'Street Address 2'
        )
        self.assertEqual(
            self.form.fields['town_city'].widget.attrs.get('placeholder'),
            'Town or City *'
        )
        self.assertEqual(
            self.form.fields['postcode'].widget.attrs.get('placeholder'),
            'Postal Code'
        )
        self.assertEqual(
            self.form.fields['county'].widget.attrs.get('placeholder'),
            'County, State or Locality'
        )

    def test_labels_are_removed(self):
        """
        Test that all labels are removed (set to False).
        """
        # Assertions
        for field in self.form.fields.values():
            self.assertFalse(field.label)

    def test_custom_country_and_email_attrs(self):
        """
        Custom attributes like aria-label and autocomplete are set.
        """
        country_attrs = self.form.fields['country'].widget.attrs
        email_attrs = self.form.fields['email'].widget.attrs

        # Assertions
        self.assertEqual(country_attrs.get('aria-label'), 'country')
        self.assertEqual(country_attrs.get('autocomplete'), 'no')
        self.assertEqual(email_attrs.get('autocomplete'), 'no')
