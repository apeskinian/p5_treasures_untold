from django.apps import AppConfig


class SupportConfig(AppConfig):
    """
    Configuration for the 'staff' app.

    This app provides a support pages for users:
    - A FAQ page.
    - A contact us page where users can submit a message with their email
        address for a reply.
    - Newsletter page where users can find out about the newsletter and enter
        their email address to sign up.
    - Privacy policy where users can read the privacy policy.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'support'
