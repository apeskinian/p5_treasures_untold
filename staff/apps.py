from django.apps import AppConfig


class StaffConfig(AppConfig):
    """
    Configuration for the 'staff' app.

    This app provides a staff dashboard where authorized users can:
    - Manage products and realms (add, edit, delete).
    - Manage FAQs and FAQ topics.
    - Read and respond to 'Contact Us' messages.
    - Create and send newsletters.
    - View and delete previously sent newsletters.
    - View current subscribers and their status.
    - Manually remove individual subscribers.
    - Clear all expired subscribers in one action.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff'
