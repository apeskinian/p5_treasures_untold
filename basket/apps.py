from django.apps import AppConfig


class BasketConfig(AppConfig):
    """
    Configuration for the 'basket' app.
    This app handles the shopping basket functionality.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
