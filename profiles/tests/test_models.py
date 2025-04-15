from django.contrib.auth.models import User
from django.test import TestCase

from ..models import UserProfile


class ProfilesModelsTests(TestCase):
    def setUp(self):
        """
        Create instances of :model:`auth.User` and
        :model:`profiles.UserProfile` for test.
        """
        self.user = User.objects.create_user(
            username='test',
            email='tesstyuza@test.com',
            password='password123',
        )
        self.user_profile, created = (
            UserProfile.objects.get_or_create(user=self.user)
        )

    def test_return_string(self):
        """
        Testing return string is the username.
        """
        self.assertEqual(str(self.user_profile), 'test')
