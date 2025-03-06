from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for the `checkout` app.
    This app manages the checkout process, including order creation and
    payment handling.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Import signals to ensure order-related signals are registered.
        """
        import checkout.signals  # noqa: F401
