from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    Stores user profile information, including default shipping details.

    **Fields:**
    - `user (OneToOneField)`: A one-to-one relationship with Django's built-in
      `User` model.
    - `default_full_name (CharField)`: The user's default full name.
    - `default_street_address_1 (CharField)`: The first line of the user's
      default street address.
    - `default_street_address_2 (CharField)`: The second line of the user's
      default street address (optional).
    - `default_town_city (CharField)`: The user's default town or city.
    - `default_county (CharField)`: The user's default county or region.
    - `default_postcode (CharField)`: The user's default postal code.
    - `default_country (CountryField)`: The user's default country.
    - `default_phone_number (CharField)`: The user's default phone number.

    **Methods:**
    - `__str__()`: Returns the associated user's username as a string.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_street_address_1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address_2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_town_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True
    )
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )

    def __str__(self):
        """
        Returns the `user.username` field as a string.

        **Returns:**
        - The `user.username` field as a string.
        """
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates or updates the user profile when a User instance is saved.

    **Arguments:**
    - `sender`: The model class that sent the signal.
    - `instance`: The actual instance of the model that was saved.
    - `created`: A boolean indicating whether the instance was created.
    - `kwargs`: Additional keyword arguments passed with the signal.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
