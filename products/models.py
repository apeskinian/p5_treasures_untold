from django.db import models
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


class Realm(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Product(models.Model):
    realm = models.ForeignKey(
        'Realm', null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    sku = models.CharField(max_length=254, null=True, blank=True)
    image = CloudinaryField(
        'image', default='placeholder', asset_folder='/treasures/',
        use_filename=True, unique_filename=False,
    )

    def __str__(self):
        return self.name
