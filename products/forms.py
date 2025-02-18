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

    new_realm = forms.CharField(
        label=False,
        required=False,
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Enter new realm name'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['price'].widget.attrs['placeholder'] = '£'

        # Setting realm names to display names in the dropdown
        realms = Realm.objects.all().order_by('name')
        display_names = [(realm.id, realm.display_name()) for realm in realms]

        self.fields['realm'].empty_label = '- Select a Realm -'
        self.fields['realm'] = forms.ChoiceField(
            choices=[
                ('', '- Select a Realm -'), ('new', 'Add New Realm')
            ] + display_names,
            required=True
        )

    def clean(self):
        cleaned_data = super().clean()
        realm = cleaned_data.get('realm')
        new_realm = cleaned_data.get('new_realm')
        new_realm_model_name = new_realm.replace(' ', '_')

        if realm == "new":
            if not new_realm:
                self.add_error('new_realm', "Please enter a new realm name.")
            else:
                realm_obj, created = (
                    Realm.objects.get_or_create(name=new_realm_model_name)
                )
                cleaned_data['realm'] = realm_obj
        else:
            try:
                cleaned_data['realm'] = Realm.objects.get(pk=int(realm))
            except Realm.DoesNotExist:
                self.add_error('realm', "Invalid realm selected.")

        return cleaned_data
