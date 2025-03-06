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
        - Set the 'name' field to autofocus.
        - Populate the 'email' field with the current user's email address if
            available.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2',
            'default_town_city': 'Town or City',
            'default_postcode': 'Postal Code',
            'default_county': 'County, State or Locality'
        }

        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country' and field != 'email':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
