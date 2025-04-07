from django.test import TestCase

from ..templatetags.product_tags import friendly_name


class ProductTagsTest(TestCase):
    def test_friendly_name(self):
        """
        Test the returned value for undescores replaced with spaces.
        """
        input = 'The_Test_to_Remove_Underscores'
        expected = 'The Test to Remove Underscores'
        self.assertEqual(friendly_name(input), expected)
