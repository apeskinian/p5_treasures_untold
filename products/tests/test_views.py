from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

from ..models import Realm, Product


class AllProductsTests(TestCase):
    def setUp(self):
        """
        Create test realms, products and client.
        """
        self.realm1 = Realm.objects.create(name='Hereington')
        self.realm2 = Realm.objects.create(name='There_Without')
        self.product1 = Product.objects.create(
            id=1,
            name='Matthew',
            realm=self.realm1,
            description='family boy',
            price=10.00,
            stock=0,
            unique_stock=True
        )
        self.product2 = Product.objects.create(
            id=2,
            name='Niamh',
            realm=self.realm1,
            description='family girl',
            price=14.00,
            stock=3
        )
        self.product3 = Product.objects.create(
            id=3,
            name='Katy',
            realm=self.realm2,
            description='friend girl',
            price=10.00,
            stock=0,
        )
        self.product4 = Product.objects.create(
            id=4,
            name='Tim',
            realm=self.realm2,
            description='friend boy',
            price=14.00,
            stock=25
        )
        self.client = Client()
        self.url = reverse('products')

    def test_viewing_all_products(self):
        """
        Testing the all products view renders the template and context.
        """
        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)

    @patch('products.models.Product.objects.annotate')
    def test_filter_products_for_new_items(self, mock_annotate):
        """
        Test to view new items. Default sorting is alphabetically and out of
        stock items are shown at the end, also sorted.
        """
        # Mocking recent dates
        recent_date = datetime(2025, 4, 10).date()
        mock_annotate.return_value.values.return_value \
            .distinct.return_value.order_by.return_value = [
                {'added_date': recent_date}
            ]

        # Mock products to return products with the recent date
        mock_filter = patch('products.models.Product.objects.filter')
        mock_filter.return_value = Product.objects.filter(
            date_added=recent_date
        )

        response = self.client.get(
            self.url, {'new': ''}
        )
        # Assertions
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)

    @patch('products.models.Product.objects.annotate')
    def test_filter_products_for_no_new_items(self, mock_annotate):
        """
        Test to view no new items.
        """
        # Mocking no new dates
        mock_annotate.return_value.values.return_value \
            .distinct.return_value.order_by.return_value = []
        response = self.client.get(
            self.url, {'new': ''}
        )
        # Assertions
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)

    def test_sorting_products_by_name_asc(self):
        """
        Test sorting products by name. Out of stock items shown last but in
        order.
        """
        response = self.client.get(
            self.url, {'sort': 'name', 'direction': 'asc'}
        )
        # Assertions
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)
        products = response.context['products']
        self.assertEqual(products.first(), self.product2)
        self.assertEqual(products.last(), self.product1)

    def test_sorting_products_by_realm_desc(self):
        """
        Test sorting products by realm name in descending order. Out of stock
        items still last but sorted.
        """
        response = self.client.get(
            self.url, {'sort': 'realm', 'direction': 'desc'}
        )
        # Assertions
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)
        products = response.context['products']
        self.assertEqual(products.first(), self.product4)
        self.assertEqual(products.last(), self.product1)

    def test_filtering_products_in_stock(self):
        """
        Test filtering products by in stock status. Result if unsorted will
        be sorted alphabetically.
        """
        response = self.client.get(
            self.url, {'stock': 'in'}
        )
        # Assertions
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)
        products = response.context['products']
        self.assertEqual(products.first(), self.product2)
        self.assertEqual(products.last(), self.product4)

    def test_filtering_products_out_stock(self):
        """
        Test filtering products by out of stock status. Result if unsorted will
        be sorted alphabetically.
        """
        response = self.client.get(
            self.url, {'stock': 'out'}
        )
        # Assertions
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)
        products = response.context['products']
        self.assertEqual(products.first(), self.product1)
        self.assertEqual(products.last(), self.product3)

    def test_filtering_products_by_realm(self):
        """
        Test filtering products by realm. Result if unsorted will be sorted
        alphabetically. Out of stock items are shown last but still ordered.
        """
        response = self.client.get(
            self.url, {'realm': 'There_Without'}
        )
        # Assertions
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)
        products = response.context['products']
        self.assertEqual(products.first(), self.product4)
        self.assertEqual(products.last(), self.product3)

    def test_search_query_results(self):
        """
        Results with matching terms in name or description will be returned.
        Ordered alphabetically by default and out of stock items at the end.
        """
        response = self.client.get(
            self.url, {'q': 'girl'}
        )
        # Assertions
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)
        products = response.context['products']
        self.assertEqual(products.first(), self.product2)
        self.assertEqual(products.last(), self.product3)

    def test_blank_search_query_results(self):
        """
        Blank search terms are ignored and a message is sent to the user.
        """
        response = self.client.get(
            self.url, {'q': '  '}
        )
        # Assertions
        self.assertRedirects(response, reverse('products'))
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Your spell needs a little more magic,' in str(msg)
            for msg in messages
        ))

    @patch('products.views.activate_reward')
    def test_bibbidi_bobbidi_boo_search_query_logged_in_user(
        self, mock_activate_reward
    ):
        """
        Blank search terms are ignored and a message is sent to the user.
        """
        # Create client, user and urls.
        self.client = Client()
        self.user = User.objects.create(
            username='TessTyuza',
            password='testpass',
            email='tess@tyuza.com'
        )
        # Log user in.
        self.client.force_login(self.user)
        self.client.get(
            self.url,
            {'q': 'bibbidi-bobbidi-boo'},
            HTTP_REFERER='http://example.com/origin/'
        )
        mock_activate_reward.assert_called_once()


class ProductDetailTests(TestCase):
    def test_product_detail_view(self):
        """
        Test the view for a product detail page.
        """
        self.realm1 = Realm.objects.create(name='Hereington')
        self.product1 = Product.objects.create(
            id=1,
            name='Matthew',
            realm=self.realm1,
            description='family boy',
            price=10.00,
            stock=1,
            unique_stock=True
        )
        self.client = Client()
        self.url = reverse('product_detail', args=[self.product1.id])

        response = self.client.get(self.url)
        # Assertions
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertIn('product', response.context)


class ActivateRewardTests(TestCase):
    def test_activate_reward_with_no_reward_input(self):
        """
        Testing error handling when no reward is sent.
        """
        self.client = Client()

        self.url = reverse(
            'activate_reward', args=['activate', None]
        )

        response = self.client.get(self.url)
        # Assertions
        self.assertEqual(response.status_code, 404)

    def test_activate_reward(self):
        """
        Testing the activation of the 'magic-lamp' reward.
        """
        self.client = Client()
        self.url = reverse('activate_reward', args=['activate', 'magic-lamp'])

        response = self.client.get(self.url)
        # Assertions
        session = self.client.session
        self.assertEqual(response.status_code, 200)
        self.assertIn('magic-lamp', session.get('rewards', []))

    def test_activate_already_active_reward(self):
        """
        Testing the activation of the 'magic-lamp' reward when it's already
        been activated.
        """
        self.client = Client()
        session = self.client.session
        session['rewards'] = ['magic-lamp']
        session.save()

        self.url = reverse('activate_reward', args=['activate', 'magic-lamp'])

        response = self.client.get(self.url)
        # Assertions
        session = self.client.session
        self.assertEqual(response.status_code, 200)
        self.assertIn('magic-lamp', session.get('rewards', []))

    def test_deactivate_already_active_reward_with_extra(self):
        """
        Testing deactivating the 'magic-lamp' reward.
        """
        self.client = Client()
        session = self.client.session
        session['rewards'] = ['magic-lamp']
        session.save()

        self.url = reverse(
            'activate_reward', args=['deactivate', 'magic-lamp', 'extra']
        )

        response = self.client.get(self.url)
        # Assertions
        session = self.client.session
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('magic-lamp', session.get('rewards', []))
