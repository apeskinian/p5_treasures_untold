from django.test import TestCase

from ..forms import OrderForm


class OrderFormTests(TestCase):
    def setUp(self):
        self.form = OrderForm()

    def test_order_form_fields(self):
        """
        Test the form includes all the expected fields.
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
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_placeholders_and_autofocus(self):
        """
        Placeholders are correct and autofocus is set on full_name.
        """
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
        All labels should be removed (set to False).
        """
        for field in self.form.fields.values():
            self.assertFalse(field.label)

    def test_custom_country_and_email_attrs(self):
        """
        Custom attributes like aria-label and autocomplete are set.
        """
        country_attrs = self.form.fields['country'].widget.attrs
        self.assertEqual(country_attrs.get('aria-label'), 'country')
        self.assertEqual(country_attrs.get('autocomplete'), 'no')

        email_attrs = self.form.fields['email'].widget.attrs
        self.assertEqual(email_attrs.get('autocomplete'), 'no')
