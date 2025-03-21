from django import forms
from django.db.models.functions import Lower

from .models import Product, Realm
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['sku', ]
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
        """
        Overide init method by adding extra choices to the realm field. This
        allows the user to create a new realm at the same time as a creating or
        adjusting a product.
        """
        super().__init__(*args, **kwargs)

        # Change placeholder of price field.
        self.fields['price'].widget.attrs['placeholder'] = '£'

        # Setting realm field choices.
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
        """
        Overrides the form's clean method to handle realm selection, allowing
        the creation of a new realm if `Add New Realm` is chosen.

        **Behavior:**
        - If `Add New Realm` is selected, a new realm is created with its name
        formatted by replacing spaces with underscores.
        - If the realm already exists it is retrieved instead of being created.
        - If an existing realm is selected, it is validated and assigned.

        **Raises:**
        - Exception: If `Add New Realm` is selected but the realm creation
            fails.
        - `Realm.DoesNotExist`: If the selected existing realm does not exist.

        **Returns:**
        - dict: The cleaned data, with the `realm` field set to either the
            new or selected realm instance.
        """
        # Set variables for method.
        cleaned_data = super().clean()
        realm = cleaned_data.get('realm')
        new_realm = cleaned_data.get('new_realm')
        new_realm_model_name = new_realm.replace(' ', '_')
        new_realm_prefix = cleaned_data.get('new_realm_prefix')

        # If 'Add New Realm' is selected, process the input from the new field.
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
                    'realm',
                    f'An error occured while processing the realm: {str(e)}'
                )
        # Process the chosen existing realm as normal.
        else:
            try:
                cleaned_data['realm'] = Realm.objects.get(pk=int(realm))
            except Realm.DoesNotExist:
                self.add_error(
                    'realm',
                    'Error selecting this realm.'
                )

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
        Overrides the form's initialization method to adjust field labels
        and placeholders.

        **Modifications:**
        - Removes the label and adds a placeholder for the `name` field.
        - Updates the label for the `the_prefix_required` field to clarify
            its purpose.
        """
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Realm name...'
        self.fields['name'].label = False
        self.fields['the_prefix_required'].label = (
            'Prefix with "the" (when grammatically applicable,'
            ' eg. Enchanted Forest)?'
        )
