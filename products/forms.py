from django import forms
from .models import Product, Realm
from .widgets import CustomClearableFileInput
from django.db.models.functions import Lower


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

    new_realm_prefix = forms.BooleanField(
        required=False,
        label=(
            'Prefix with "the" (when grammatically applicable, '
            'e.g. Enchanted Forest)?'
        ),
        widget=forms.CheckboxInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['price'].widget.attrs['placeholder'] = '£'

        # Setting realm names to display names in the dropdown
        realms = Realm.objects.all().order_by(Lower('name'))
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
        new_realm_prefix = cleaned_data.get('new_realm_prefix')

        if realm == "new":
            try:
                realm_obj, created = (
                    Realm.objects.get_or_create(
                        name=new_realm_model_name,
                        the_prefix_required=new_realm_prefix
                    )
                )
                cleaned_data['realm'] = realm_obj
            except Exception as e:
                self.add_error(
                    None,
                    'An error occured while processing the new realm: '
                    f'{str(e)}'
                )
        else:
            try:
                cleaned_data['realm'] = Realm.objects.get(pk=int(realm))
            except Realm.DoesNotExist:
                self.add_error(None, "Invalid realm selected.")

        return cleaned_data


class RealmForm(forms.ModelForm):
    class Meta:
        model = Realm
        fields = (
            'name',
            'the_prefix_required'
        )

    def __init__(self, *args, **kwargs):
        """
        add placeholders and remove auto-generated label
        """
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Realm name...'
        self.fields['name'].label = False
        self.fields['the_prefix_required'].label = (
            'Prefix with "the" (when grammatically applicable,'
            ' eg. Enchanted Forest)?'
        )
