from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Configuration for the `products` app.
    This app handles the products.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        """
        Import signal handlers to ensure they are registered when the app is
        ready. This allows the `products` app to trigger custom signals where
        necessary.
        """
        import products.signals  # noqa: F401
