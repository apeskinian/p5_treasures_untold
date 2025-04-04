from decimal import Decimal

from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory

from products.models import Product, Realm
from ..contexts import basket_contents


class BasketContentsTest(TestCase):
    def setUp(self):
        """
        Set up request, realm and products for test.
        """
        # Create a mock request
        self.factory = RequestFactory()

        # Create test realm
        self.agrabah = Realm.objects.create(
            name='Agrabah',
        )
        self.atlantica = Realm.objects.create(
            name='Atlantica',
        )

        # Create test products
        self.product1 = Product.objects.create(
            id=1,
            name='Magic Lamp',
            realm=self.agrabah,
            description='product descripton',
            price=10.00,
            stock=1,
            unique_stock=True
        )
        self.product2 = Product.objects.create(
            id=2,
            name='Left Half of a Golden Scarab Beetle',
            realm=self.agrabah,
            description='product descripton',
            price=10.00,
            stock=1,
            unique_stock=True
        )
        self.product3 = Product.objects.create(
            id=3,
            name='Dinglehopper',
            realm=self.atlantica,
            description='product descripton',
            price=10.00,
            stock=5
        )
        self.product4 = Product.objects.create(
            id=4,
            name='Right Half of a Golden Scarab Beetle',
            realm=self.agrabah,
            description='product descripton',
            price=10.00,
            stock=1,
            unique_stock=True
        )

    def get_request_with_basket_and_reward(self, basket, rewards=None):
        """
        Function to create a request with basket and rewards session data.
        """
        # Creating the request and session to attach to the request.
        request = self.factory.get('/')
        middleware = SessionMiddleware(lambda req: None)
        middleware.process_request(request)
        request.session.save()

        # Set session info for request from provided arguments
        request.session['basket'] = basket
        request.session['rewards'] = rewards or []
        request.session.save()

        return request

    def test_basket_contents_no_rewards(self):
        """
        Testing the basket context with no rewards activated.
        """
        # Get a basket with the Magic Lamp and 4 Dinglehoppers
        request = self.get_request_with_basket_and_reward({
            str(self.product1.pk): 1,
            str(self.product3.pk): 4
        })

        context = basket_contents(request)

        self.assertEqual(len(context['basket_items']), 2)
        self.assertEqual(context['rewards'], [])
        self.assertEqual(context['original_total'], Decimal(0))
        self.assertEqual(context['total'], Decimal(50))
        self.assertEqual(context['product_count'], 5)
        self.assertEqual(context['delivery'], settings.DELIVERY)
        self.assertEqual(
            context['grand_total'], Decimal(50)+Decimal(settings.DELIVERY)
        )

    def test_basket_with_bibbidi_bobbidi_boo_reward(self):
        """
        Testing the 20% discount applied with the 'Bibbidi-Bobbidi-Boo' reward.
        """
        # Get a basket with 5 Dinglehoppers and the reward applied.
        request = self.get_request_with_basket_and_reward({
            str(self.product3.pk): 5
        }, 'bibbidi-bobbidi-boo')

        context = basket_contents(request)

        self.assertEqual(len(context['basket_items']), 1)
        self.assertEqual(context['rewards'], 'bibbidi-bobbidi-boo')
        self.assertEqual(context['original_total'], Decimal(50))
        self.assertEqual(
            context['total'].quantize(Decimal('0.01')), Decimal(40)
        )
        self.assertEqual(context['product_count'], 5)
        self.assertEqual(context['delivery'], settings.DELIVERY)
        self.assertEqual(
            context['grand_total'].quantize(Decimal('0.01')),
            Decimal(40)+Decimal(settings.DELIVERY)
        )

    def test_basket_with_magic_lamp_reward(self):
        """
        Testing the first three items are free with the 'Magic Lamp' reward.
        """
        # Get a basket with 5 Dinglehoppers and the reward applied.
        request = self.get_request_with_basket_and_reward({
            str(self.product1.pk): 1,
            str(self.product2.pk): 1,
            str(self.product3.pk): 4,
            str(self.product4.pk): 1
        }, 'magic-lamp')

        context = basket_contents(request)

        # Check that only first three products prices are 0
        for index, (item) in enumerate(context['basket_items']):
            if index < 3:
                self.assertEqual(item['product'].price, Decimal(0))
            else:
                self.assertEqual(item['product'].price, Decimal(10))

        # Check context
        self.assertEqual(len(context['basket_items']), 4)
        self.assertEqual(context['rewards'], 'magic-lamp')
        self.assertEqual(context['original_total'], Decimal(0))
        self.assertEqual(
            context['total'].quantize(Decimal('0.01')), Decimal(10)
        )
        self.assertEqual(context['product_count'], 7)
        self.assertEqual(context['delivery'], settings.DELIVERY)
        self.assertEqual(
            context['grand_total'].quantize(Decimal('0.01')),
            Decimal(10)+Decimal(settings.DELIVERY)
        )

    def test_basket_with_cave_of_wonders_reward(self):
        """
        Testing items from Agrabah are free with the 'Cave of Wonders' reward.
        """
        # Get a basket with 5 Dinglehoppers and the reward applied.
        request = self.get_request_with_basket_and_reward({
            str(self.product1.pk): 1,
            str(self.product2.pk): 1,
            str(self.product3.pk): 3,
            str(self.product4.pk): 1
        }, 'cave-of-wonders')

        context = basket_contents(request)

        # Check that items from Agrabah are now free
        for item in context['basket_items']:
            if item['product'].realm.name == 'Agrabah':
                self.assertEqual(item['product'].price, Decimal(0))
            if item['product'].realm.name != 'Agrabah':
                self.assertEqual(item['product'].price, Decimal(10))

        # Check context
        self.assertEqual(len(context['basket_items']), 4)
        self.assertEqual(context['rewards'], 'cave-of-wonders')
        self.assertEqual(context['original_total'], Decimal(0))
        self.assertEqual(
            context['total'].quantize(Decimal('0.01')), Decimal(30)
        )
        self.assertEqual(context['product_count'], 6)
        self.assertEqual(context['delivery'], settings.DELIVERY)
        self.assertEqual(
            context['grand_total'].quantize(Decimal('0.01')),
            Decimal(30)+Decimal(settings.DELIVERY)
        )
