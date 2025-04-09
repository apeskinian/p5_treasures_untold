from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase, Client
from django.urls import reverse

from ..models import UserProfile
from checkout.models import Order


class ProfileTests(TestCase):
    def setUp(self):
        # Create client, user, profile, order and url
        self.client = Client()
        self.user = User.objects.create(
            username='TessTyuza',
            password='testpass',
            email='tess@tyuza.com'
        )
        self.profile, created = (
            UserProfile.objects.get_or_create(user=self.user)
        )
        self.order = Order.objects.create(
            order_number='12345',
            user_profile=self.profile,
            full_name='Tess Tyuza',
            email='tess@tyuza.com',
            street_address_1='Street',
            town_city='Town',
            country='GB',
            delivery_cost=10.00,
            order_total=100.00,
            grand_total=110.00
        )
        self.url = reverse('profile')

    def test_login_required(self):
        """
        Test that the view requires login.
        """
        # Try to access the profile view without logging in.
        response = self.client.get(self.url)
        # Assertions
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_profile_view(self):
        """
        Test viewing profile page.
        """
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertIn('form', response.context)
        self.assertIn('orders', response.context)
        self.assertIn('profile', response.context)
        self.assertIsNone(response.context['view_order'])

    def test_previous_order_view(self):
        """
        Test viewing previous order details.
        """
        self.client.force_login(self.user)
        url = reverse(
            'order_history', kwargs={'order_number': self.order.order_number}
        )
        response = self.client.get(url)
        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['view_order'], self.order)

    def test_valid_profile_update(self):
        """
        Test updating profile with valid data.
        """
        self.client.force_login(self.user)
        response = self.client.post(self.url, {
            'default_full_name': 'Tess Tyuza',
            'default_phone_number': '123456'
        })
        # Assertions
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Profile updated.' in str(msg)
            for msg in messages
        ))
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_full_name, 'Tess Tyuza')
        self.assertEqual(self.profile.default_phone_number, '123456')

    def test_invalid_profile_update(self):
        """
        Test updating profile with invalid data.
        """
        self.client.force_login(self.user)
        response = self.client.post(self.url, {
            'default_country': '345',
        })
        # Assertions
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Update failed. Please ensure the form is valid' in str(msg)
            for msg in messages
        ))
