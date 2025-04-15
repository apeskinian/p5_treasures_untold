from decimal import Decimal

from django.test import TestCase

from ..templatetags.checkout_tools import calc_original_total


class CheckoutToolsTest(TestCase):
    def test_calc_original_total(self):
        """
        Test the calculation of an input to return 100% when given 80%.
        """
        original_cost = Decimal(10)
        discounted_cost = Decimal(original_cost*Decimal(0.8))
        self.assertEqual(calc_original_total(discounted_cost), original_cost)
