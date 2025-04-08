from django.core.exceptions import ValidationError
from django.test import TestCase, override_settings
from unittest.mock import patch, MagicMock
from django.templatetags.static import static

from ..models import Realm, Product


class ReamModelTests(TestCase):
    def setUp(self):
        """
        Create a realm for testing.
        """
        self.test_realm = Realm.objects.create(
            name='Test_Realm'
        )

    def test_name_return(self):
        """
        Test to check the return string.
        """
        self.assertEqual(str(self.test_realm), 'Test_Realm')

    def test_display_name(self):
        """
        Testing display name creation.
        """
        self.assertEqual(self.test_realm.display_name(), 'Test Realm')


class ProductModelTests(TestCase):
    def setUp(self):
        """
        Create test realm and products.
        """
        self.test_realm = Realm.objects.create(
            name='Test_Realm'
        )
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            realm=self.test_realm,
            description='product descripton',
            price=10.00,
            stock=1,
            unique_stock=True,
            sku='ID123'
        )
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            realm=self.test_realm,
            description='product descripton',
            price=14.00,
            stock=3,
            unique_stock=True
        )

    def test_name_return(self):
        """
        Test the string return.
        """
        self.assertEqual(str(self.product1), 'test product 1')

    def test_realma_name(self):
        """
        Test realm name returned.
        """
        self.assertEqual(self.product1.realm_name(), 'Test Realm')

    @override_settings(DEBUG=True)
    def test_placeholder_image_url_assignment_debug_on(self):
        """
        Test image_url for placeholder images with debug on.
        """
        self.product1.image = 'placeholder'
        self.assertEqual(
            self.product1.image_url, static('images/dev_placeholder.png')
        )

    @override_settings(DEBUG=True)
    def test_custom_image_url_assignment_debug_on(self):
        """
        Test image_url for custom images with debug on.
        """
        self.product1.image = 'custom_image'
        self.assertEqual(
            self.product1.image_url, static(
                f'images/dev_mode/{self.product1.sku}.png'
            )
        )

    @override_settings(DEBUG=False)
    def test_placeholder_image_url_assignment_debug_off(self):
        """
        Test image_url for custom images with debug off.
        """
        self.product1.image = 'placeholder'
        self.assertEqual(
            self.product1.image_url, static('images/placeholder.png')
        )

    @override_settings(DEBUG=False)
    @patch('products.models.cloudinary_url')
    def test_cloudinary_url_assignment_debug_off(self, mock_cloudinary_url):
        """
        Test image_url for custom images with cloudinary urls and debug off.
        """
        # Creating the test cloudinary image and url.
        mock_image = MagicMock()
        mock_image.public_id = 'test_public_id'
        self.product1.image = mock_image
        mock_cloudinary_url.return_value = [
            'https://res.cloudinary.com/test_url'
        ]

        # Asserstions.
        self.assertEqual(
            self.product1.image_url,
            'https://res.cloudinary.com/test_url'
        )
        mock_cloudinary_url.assert_called_once_with(
            'test_public_id',
            secure=True,
            fetch_format='auto',
            quality='auto:best',
            width=500,
            height=500,
            crop='fill'
        )

    def test_unique_stock_exception_handling_on_clean(self):
        """
        Test the model clean method to handle stock more than one for unique
        products.
        """
        with self.assertRaises(ValidationError):
            self.product2.clean()
