from django import forms
from .models import Product, Realm
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['sku',]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setting realm names to display names in the dropdown
        realms = Realm.objects.all().order_by('name')
        display_names = [(r.id, r.display_name()) for r in realms]
        self.fields['realm'].choices = display_names
        self.fields['price'].widget.attrs['placeholder'] = '£'
