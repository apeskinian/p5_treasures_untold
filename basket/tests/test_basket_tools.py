from django.test import TestCase

from ..templatetags.basket_tools import calc_subtotal


class CalcSubtotalTest(TestCase):
    def test_subtotal_calculation(self):
        """
        Test the subtotal calculation.
        """
        self.assertEqual(calc_subtotal(5, 10), 50)
