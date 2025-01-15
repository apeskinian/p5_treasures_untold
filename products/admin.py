from django.contrib import admin
from .models import Realm, Product

# registering models
admin.site.register(Realm)
admin.site.register(Product)
