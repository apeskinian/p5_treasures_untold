from django.db import models
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


class Realm(models.Model):
    name = models.CharField(max_length=254)
    the_prefix_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def display_name(self):
        return self.name.replace('_', ' ')


class Product(models.Model):
    realm = models.ForeignKey(
        'Realm', null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    image = CloudinaryField(
        'image', default='placeholder', asset_folder='/treasures/',
        use_filename=True, unique_filename=False
    )
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def realm_name(self):
        return self.realm.name.replace('_', ' ')
