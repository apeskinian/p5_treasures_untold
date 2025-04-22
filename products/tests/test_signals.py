from unittest.mock import MagicMock, patch

from django.test import TestCase

from ..models import Product


class ProductsSignalTests(TestCase):
    def setUp(self):
        """
        Create instances of :model:`products.Product` and images with
        public ids for tests.
        """
        # Create product
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product description',
            price=10.00,
            stock=1,
            unique_stock=True,
        )
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            description='product description',
            price=10.00,
            stock=1,
            unique_stock=True,
        )
        # Create image with public id to delete.
        self.mock_image1 = MagicMock()
        self.mock_image1.public_id = 'test_public_id'
        self.product1.image = self.mock_image1
        # Create image with placeholder id so shouldn't be deleted.
        self.mock_image2 = MagicMock()
        self.mock_image2.public_id = 'placeholder'
        self.product2.image = self.mock_image2

    @patch('products.signals.destroy')
    def test_cloudinary_delete(self, mock_destroy):
        """
        Test calling the cloudinary `destroy` method if public id is not
        'placeholder'
        """
        self.product1.delete()

        # Assertions
        mock_destroy.assert_called_once_with('test_public_id')

    @patch('products.signals.destroy')
    def test_cloudinary_no_delete(self, mock_destroy):
        """
        Test to check that when public is 'placeholder' that the `destroy`
        method is not called.
        """
        self.product2.delete()

        # Assertions
        mock_destroy.assert_not_called()
