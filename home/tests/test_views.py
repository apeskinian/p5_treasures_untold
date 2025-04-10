from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

from products.models import Realm, Product


class IndexTests(TestCase):
    def setUp(self):
        # Create client and URL
        self.client = Client()
        self.user = User.objects.create(
            username='TessTyuza',
            password='testpass',
            email='tess@tyuza.com'
        )
        self.client.force_login(self.user)
        self.url = reverse('home')
        # Create products and realm
        self.realm = Realm.objects.create(name='Test_Realm')
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            realm=self.realm,
            description='product descripton',
            price=10.00,
            stock=0,
            unique_stock=True
        )
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            realm=self.realm,
            description='product descripton',
            price=14.00,
            stock=3
        )

    @patch('products.models.Product.objects.annotate')
    def test_home_view_no_new_products(self, mock_annotate):
        """
        Testing the homepage view with no new products.
        """
        # Mocking no new dates
        mock_annotate.return_value.values.return_value \
            .distinct.return_value.order_by.return_value = []
        # Get the response
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertIn('current_user', response.context)
        self.assertIn('featured_realm', response.context)
        self.assertIn('featured_products', response.context)

    @patch('products.models.Product.objects.annotate')
    def test_home_view_new_products(self, mock_annotate):
        """
        Testing the homepage view with new products.
        """
        # Mocking the recent dates
        mock_annotate_return = mock_annotate.return_value
        mock_values_return = mock_annotate_return.values.return_value
        mock_distinct_return = mock_values_return.distinct.return_value
        mock_order_by_return = mock_distinct_return.order_by.return_value
        mock_order_by_return[:] = [{'added_date': '2025-04-09'}]
        # Get the response
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertIn('current_user', response.context)
        self.assertIn('new_products', response.context)
        self.assertIn('featured_realm', response.context)
        self.assertIn('featured_products', response.context)
