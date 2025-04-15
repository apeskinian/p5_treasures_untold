from datetime import datetime

from django.contrib.sessions.backends.db import SessionStore
from django.test import TestCase, RequestFactory

from ..middleware import UpdateSessionMiddleware


class UpdateSessionMiddelwareTest(TestCase):
    def setUp(self):
        """
        Sets up a request and session for tests.
        """
        self.middleware = UpdateSessionMiddleware(lambda x: None)
        self.factory = RequestFactory()

        self.session1 = SessionStore()
        self.session1.save()

        self.request = self.factory.get('/')
        self.request.session = self.session1

    def test_modified_session_data(self):
        """
        Testing that the middleware updates the session with a 'modified'
        timestamp.
        """
        # Call the middlware.
        self.middleware(self.request)

        # Assertions
        self.assertTrue('modified' in self.request.session)
        self.assertTrue(self.request.session.modified)
        # Check timestamp format.
        timestamp = self.request.session['modified']
        try:
            datetime.strptime(timestamp, '%d/%m/%Y, %H:%M:%S')
        except ValueError:
            self.fail(f"Timestamp format is incorrect: {timestamp}")
