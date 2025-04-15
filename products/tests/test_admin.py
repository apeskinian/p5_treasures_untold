from unittest.mock import Mock

from django.test import TestCase, RequestFactory

from products.models import Product

from ..admin import ProductAdmin


class RestockProductAdminActionTest(TestCase):
    def setUp(self):
        """
        Create request and instances of :model:`products.Product` for tests.
        """
        # Create request.
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        # Create test products.
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product descripton',
            price=10.00,
            stock=0,
            unique_stock=True
        )
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            description='product descripton',
            price=14.00,
            stock=3
        )
        self.product3 = Product.objects.create(
            id=3,
            name='test product 3',
            description='product descripton',
            price=10.00,
            stock=1,
        )
        self.product4 = Product.objects.create(
            id=4,
            name='test product 4',
            description='product descripton',
            price=14.00,
            stock=25
        )
        # Mock modeladmin object.
        self.modeladmin = Mock()

    def test_product_restock(self):
        """
        Test for product restock. Unique items should be restocked to 1 and
        all other to 50.
        """
        queryset = [
            self.product1,
            self.product2,
            self.product3,
            self.product4
        ]
        # Call the restock action
        ProductAdmin.restock(self.modeladmin, self.request, queryset)

        # Refresh product stock from db.
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()
        self.product3.refresh_from_db()
        self.product4.refresh_from_db()

        # Assertions
        self.assertEqual(self.product1.stock, 1)
        self.assertEqual(self.product2.stock, 50)
        self.assertEqual(self.product3.stock, 50)
        self.assertEqual(self.product4.stock, 50)
