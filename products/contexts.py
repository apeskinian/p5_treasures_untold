from django.db.models.functions import Lower

from .models import Realm


def get_realms(request):
    """
    Provides global access to all realms in the app, ordered case-insensitively
    by name.

    **Arguments:**
    - `request`: The HTTP request.

    **Returns:**
    - A dictionary containing:
        - `'all_realms'`: A queryset of :model:`products.Realm`, ordered
        case-insensitively by name.
    """
    all_realms = Realm.objects.all().order_by(Lower('name'))
    return {'all_realms': all_realms}
