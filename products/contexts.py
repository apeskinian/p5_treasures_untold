from .models import Realm
from django.db.models.functions import Lower


def get_realms(request):
    """
    returns a queryset of all current realms in db sorted alphabetically
    """
    all_realms = Realm.objects.all().order_by(Lower('name'))
    return {'all_realms': all_realms}
