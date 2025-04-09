from django.core.management import call_command
from django.test import TestCase
from io import StringIO


class ClearAbandonedSessionsTests(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('clear_abandoned_sessions', stdout=out)
        self.assertIn('Recovered', out.getvalue())
