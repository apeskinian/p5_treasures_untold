import re

from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    email = forms.CharField(required=False, disabled=True)

    class Meta:
        model = UserProfile
        fields = [
            'default_full_name',
            'default_phone_number',
            'default_street_address_1',
            'default_street_address_2',
            'default_town_city',
            'default_postcode',
            'default_county',
            'default_country'
        ]

    def __init__(self, *args, **kwargs):
        """
        Override the initialization method to customize form behavior:
        - Set placeholders for specific fields.
        - Remove labels from all fields.
        - Set the `name` field to autofocus.
        - Populate the `email` field with the current user's email address if
            available.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number (e.g. +441234567890)',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2',
            'default_town_city': 'Town or City',
            'default_postcode': 'Postal Code',
            'default_county': 'County, State or Locality'
        }

        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

        for field in self.fields:
            if field != 'default_country' and field != 'email':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
        self.fields['email'].widget.attrs['aria-label'] = 'email'
        self.fields['default_country'].widget.attrs['aria-label'] = 'country'

    def clean(self):
        """
        Overrides the clean method to check telephone numbers conform to E.164.
        """
        # Set variables for method.
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('default_phone_number')

        if phone_number:
            if not re.fullmatch(r'^\+[1-9]\d{1,14}$', phone_number):
                self.add_error(
                    'default_phone_number',
                    'Phone number must be in E.164 format (e.g. +1234567890).'
                )
            else:
                cleaned_data['default_phone_number'] = phone_number

        return cleaned_data
