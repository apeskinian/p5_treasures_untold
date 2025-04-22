import re

from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address_1',
            'street_address_2',
            'town_city',
            'county',
            'postcode',
            'country',
        )

    def __init__(self, *args, **kwargs):
        """
        Initialize the order form with custom placeholders, remove
        auto-generated labels, and set autofocus on the `full_name` field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number (e.g. +123456789012345)',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'town_city': 'Town or City',
            'postcode': 'Postal Code',
            'county': 'County, State or Locality'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
        self.fields['country'].widget.attrs['aria-label'] = 'country'
        self.fields['country'].widget.attrs['autocomplete'] = 'no'
        self.fields['email'].widget.attrs['autocomplete'] = 'no'

    def clean(self):
        """
        Overrides the clean method to check telephone numbers conform to E.164.
        """
        # Set variables for method.
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')

        if phone_number:
            if not re.fullmatch(r'^\+[1-9]\d{1,14}$', phone_number):
                self.add_error(
                    'phone_number',
                    'Phone number must be in E.164 format '
                    '(e.g. +123456789012345).'
                )
            else:
                cleaned_data['phone_number'] = phone_number

        return cleaned_data
