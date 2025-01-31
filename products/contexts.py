from .models import Realm


def get_realms(request):
    """
    returns a queryset of all current realms in db sorted alphabetically
    """
    all_realms = Realm.objects.all().order_by('name')
    return {'all_realms': all_realms}
