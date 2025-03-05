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
        '''
        Initialize the order form with custom placeholders, remove
        auto-generated labels, and set autofocus on the 'full_name' field.
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
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
