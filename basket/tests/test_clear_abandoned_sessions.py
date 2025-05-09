from datetime import datetime, timedelta
from io import StringIO

from django.contrib.sessions.backends.db import SessionStore
from django.core.management import call_command
from django.test import TestCase

from products.models import Product


class ClearAbandonedSessionsTests(TestCase):
    def setUp(self):
        """
        Create :model:`products.Product` instances and a session for testing.
        """
        self.command = 'clear_abandoned_sessions'
        # Create test products
        self.product1 = Product.objects.create(
            id=1,
            name='test product 1',
            description='product description',
            price=10.00,
            stock=0,
            unique_stock=True
        )
        self.product2 = Product.objects.create(
            id=2,
            name='test product 2',
            description='product description',
            price=14.00,
            stock=3
        )
        # Creating fake times
        now = datetime.now()
        self.fake_expiry = now - timedelta(hours=2)

        # Create test session with basket contents
        self.session1 = SessionStore()
        self.session1['basket'] = {'1': 1, '2': 2}
        self.session1.save()

    def test_no_timestamp(self):
        """
        Test the error handling for session with no timestamp.
        """
        # Call command
        out = StringIO()
        call_command(self.command, stdout=out)

        # Assertions
        self.assertIn('Skipping session', out.getvalue())

    def test_invalid_timestamp_format(self):
        """
        Test the error handling for incorrect timestamp format.
        """
        self.session1['modified'] = (
            datetime.now().strftime('%d/%m/%Y, %H:%M')
        )
        self.session1.save()
        # Call command
        out = StringIO()
        err = StringIO()
        call_command(self.command, stdout=out, stderr=err)

        # Assertions
        self.assertIn('Invalid modified format', err.getvalue())

    def test_valid_timestamp_format_and_basket_clearance(self):
        """
        Test for a successful basket clearance. Session has correct timestamp
        and basket info.
        """
        # Add timestamp to session
        self.session1['modified'] = (
            self.fake_expiry.strftime('%d/%m/%Y, %H:%M:%S')
        )
        self.session1.save()
        # Call command
        out = StringIO()
        call_command(self.command, stdout=out)

        # Refresh product stock
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()

        # Assertions
        self.assertIn('Recovered', out.getvalue())
        self.assertEqual(self.product1.stock, 1)
        self.assertEqual(self.product2.stock, 5)

    def test_catching_overstocking_for_unique_and_negative_restock(self):
        """
        Testing error handling for overstock and negative stock events as a
        result of recovering stock.
        """
        # Adjust basket contents to force the errors.
        self.session1['basket'] = {'1': 2, '2': -10}
        self.session1['modified'] = (
            self.fake_expiry.strftime('%d/%m/%Y, %H:%M:%S')
        )
        self.session1.save()
        # Call command.
        out = StringIO()
        err = StringIO()
        call_command(self.command, stdout=out, stderr=err)

        # Refresh product stock
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()

        # Assertions
        self.assertIn('Error updating stock for', err.getvalue())
        self.assertEqual(self.product1.stock, 1)
        self.assertEqual(self.product2.stock, 0)
