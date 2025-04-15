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

    def save(self, commit=True):
        """
        Overrides the form's save method to handle new realm creation.

        **Behavior:**
        - If there is a new realm, it is created and replaces the placholder
            realm that was set in the clean method.

        **Raises:**
        - Exception: If there is problem creating and assigning the new realm.

        **Returns:**
        - instance: The updated instance of :form:`products.ProductForm` with a
            new realm selected if one was created.
        """
        instance = super().save(commit=False)

        # Check for cleaned new realm info
        new_realm_name = self.cleaned_data.get('new_realm', '').strip()
        new_realm_prefix = self.cleaned_data.get('new_realm_prefix')

        # If a new realm name exists, create the realm and assign it to the
        # product.
        if new_realm_name:
            try:
                realm_obj, created = (
                    Realm.objects.get_or_create(
                        name=new_realm_name.replace(' ', '_'),
                        the_prefix_required=new_realm_prefix
                    )
                )
                instance.realm = realm_obj
            except Exception as e:
                self.add_error('realm', f'An error occured: {str(e)}')

        if commit:
            instance.save()
        return instance

    def clean(self):
        """
        Overrides the form's clean method to handle realm selection, allowing
        the creation of a new realm if `Add New Realm` is chosen.

        **Behavior:**
        - If `Add New Realm` is selected, a placeholder realm is used to pass
         form validation so that a new realm can be created in the save method.
        - If an existing realm is selected, it is validated and assigned.

        **Raises:**
        - Error: If the new realm name is invalid.
        - Exception: If `Add New Realm` is selected but the realm placeholder
            fails.
        - `Realm.DoesNotExist`: If the selected existing realm does not exist.

        **Returns:**
        - dict: The cleaned data, with the `realm` field set to either the
            placeholder or selected realm instance.
        """
        # Set variables for method.
        cleaned_data = super().clean()
        realm = cleaned_data.get('realm')
        new_realm = cleaned_data.get('new_realm', '').strip()

        # If 'Add New Realm' is selected check for invalid input first.
        if realm == 'new' and not new_realm:
            self.add_error(
                'realm',
                'Realm name cannot be blank.'
            )
        # If there is a valid new realm name, use an existing realm as a
        # placeholder first to pass form validation.
        elif realm == 'new':
            try:
                cleaned_data['realm'] = Realm.objects.first()
            except Exception as e:
                self.add_error(
                    'realm',
                    f'An error occured while processing the realm: {str(e)}'
                )
        # Otherwise process the chosen existing realm as normal.
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

    def save(self, commit=True):
        """
        Overrides the form's save method to handle the realm name.

        **Behavior:**
        - Updates the name field to replace spaces with underscores.

        **Returns:**
        - instance: The form instance with `name` field updated to have
              spaces replaced with underscores.
        """
        print('CALLED')
        instance = super().save(commit=False)
        print(instance)
        if instance.name:
            instance.name = instance.name.replace(' ', '_')

        if commit:
            instance.save()
        return instance
