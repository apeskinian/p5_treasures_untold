from unittest.mock import patch

from django.test import TestCase

from products.models import Realm

from ..forms import RealmForm, ProductForm


class RealmFormTests(TestCase):
    def setUp(self):
        """
        Create an instance of :form:`products.RealmForm` for tests.
        """
        self.form = RealmForm()

    def test_for_fields(self):
        """
        Check the instance of :form:`products.RealmForm` has the
        expected fields.
        """
        expected_fields = [
            'name',
            'the_prefix_required'
        ]

        # Assertions
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_save_method(self):
        """
        Test the save method to confirm it replaces spaces with underscores.
        """
        # Create form data.
        form_data = {'name': 'Test Realm Name'}
        form = RealmForm(data=form_data)
        saved_instance = form.save(commit=True)

        # Assertions
        self.assertEqual(saved_instance.name, 'Test_Realm_Name')


class ProductFormTests(TestCase):
    def setUp(self):
        """
        Create instaces of :model:`products.Realm` and
        :form:`products.RealmForm` for the tests.
        """
        # Create test realms.
        self.realm_a = Realm.objects.create(name='Realm_A')
        self.realm_b = Realm.objects.create(name='Realm_B')
        # Create test form.
        self.form = ProductForm()

    def test_for_fields(self):
        """
        Check the instance of :form:`products.RealmForm` has the
        expected fields.
        """
        expected_fields = [
            'name',
            'realm',
            'description',
            'price',
            'stock',
            'image',
            'unique_stock',
            'new_realm',
            'new_realm_prefix'
        ]

        # Assertions
        self.assertEqual(list(self.form.fields.keys()), expected_fields)

    def test_placeholder_for_price(self):
        """
        Check placeholder for price field.
        """
        # Assertions
        self.assertEqual(
            self.form.fields['price'].widget.attrs.get('placeholder'),
            '£'
        )

    def test_realm_field_choices(self):
        """
        Confirm the realm choices include the add new realm options.
        """
        realm_choices = self.form.fields['realm'].choices
        expected_choices = [
            ('', '- Select a Realm -'),
            ('new', 'Add New Realm'),
            (1, 'Realm A'),
            (2, 'Realm B')
        ]

        # Assertions
        self.assertEqual(realm_choices, expected_choices)

    def test_save_method_with_new_realm(self):
        """
        Testing the save method creates and applies a new realm.
        """
        # Create form data.
        form_data = {
            'name': 'Test Product',
            'realm': 'new',
            'description': 'Test Description',
            'price': '3.00',
            'stock': '4',
            'new_realm': 'Realm C'
            }
        form = ProductForm(data=form_data)
        saved_instance = form.save(commit=True)

        # Assertions
        self.assertTrue(Realm.objects.filter(name='Realm_C').exists())
        self.assertEqual(str(saved_instance.realm), 'Realm_C')

    def test_save_method_with_invalid_new_realm(self):
        """
        Testing the save method with patched exception.
        """
        # Create form data.
        form_data = {
            'name': 'Test Product',
            'realm': 'new',
            'description': 'Test Description',
            'price': '3.00',
            'stock': '4',
            'new_realm': 'Realm C'
            }
        # Patch get_or_create to raise an exception
        with patch(
            'products.forms.Realm.objects.get_or_create',
            side_effect=Exception()
        ):
            # Create form and assert validity.
            form = ProductForm(data=form_data)
            instance = form.save(commit=True)

            # Assertions for errors.
            self.assertIsNotNone(instance)
            self.assertIn('realm', form.errors)
            self.assertIn('An error occurred:', form.errors['realm'][0])

    def test_clean_method_new_selected_blank_input(self):
        """
        Testing the clean method for new realm selection but blank input.
        """
        # Create form data.
        form_data = {
            'name': 'Test Product',
            'realm': 'new',
            'description': 'Test Description',
            'price': '3.00',
            'stock': '4',
            'new_realm': '   '
            }
        # Create form.
        form = ProductForm(data=form_data)

        # Assertions.
        self.assertFalse(form.is_valid())
        self.assertIn('realm', form.errors)
        self.assertIn('Realm name cannot be blank.', form.errors['realm'][0])

    def test_clean_method_new_selected_exception_for_placeholder(self):
        """
        Testing the clean method for new realm selection exception
        handling by simulating an exception when assigning the placeholder
        realm.
        """
        # Create form data.
        form_data = {
            'name': 'Test Product',
            'realm': 'new',
            'description': 'Test Description',
            'price': '3.00',
            'stock': '4',
            'new_realm': 'Realm C'
            }
        # Patch first() to raise an exception
        with patch(
            'products.forms.Realm.objects.first',
            side_effect=Exception()
        ):
            # Create form.
            form = ProductForm(data=form_data)

            # Assertions
            self.assertFalse(form.is_valid())
            self.assertIn('realm', form.errors)
            self.assertIn(
                'An error occurred while processing the realm:',
                form.errors['realm'][0]
            )

    def test_clean_method_with_existing_realm(self):
        """
        Testing the clean method with valid existing realm selected.
        """
        # Create form data.
        form_data = {
            'name': 'Test Product',
            'realm': '2',
            'description': 'Test Description',
            'price': '3.00',
            'stock': '4',
            }
        form = ProductForm(data=form_data)
        saved_instance = form.save(commit=True)

        # Assertions
        self.assertEqual(str(saved_instance.realm), 'Realm_B')

    def test_clean_method_exception_for_existing_realm(self):
        """
        Testing the clean method for choosing an existing realm exception
        handling. The exception is simulated in `objects.get()`
        """
        # Create form data.
        form_data = {
            'name': 'Test Product',
            'realm': '2',
            'description': 'Test Description',
            'price': '3.00',
            'stock': '4',
            }
        # Patch get() to raise an exception
        with patch(
            'products.forms.Realm.objects.get',
            side_effect=Realm.DoesNotExist()
        ):
            # Create form.
            form = ProductForm(data=form_data)

            # Assertions
            self.assertFalse(form.is_valid())
            self.assertIn('realm', form.errors)
            self.assertIn(
                'Error selecting this realm.',
                form.errors['realm'][0]
            )
