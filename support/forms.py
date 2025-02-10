from django import forms
from .models import contactMessage


class contactForm(forms.ModelForm):

    class Meta:
        model = contactMessage
        fields = [
            'name', 'email', 'message'
        ]

    def __init__(self, *args, **kwargs):
        """
        add placeholders, remove auto-generated labels and set
        autofocus  on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email',
            'message': 'Type your message here...'
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
