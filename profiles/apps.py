from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration for the 'profiles' app.
    This app handles the user profiles including viewing order history and
    updating stored details.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
