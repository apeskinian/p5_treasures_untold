from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.templatetags.static import static


class Realm(models.Model):
    name = models.CharField(max_length=254)
    the_prefix_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def display_name(self):
        return self.name.replace('_', ' ')


class Product(models.Model):
    name = models.CharField(max_length=254)
    realm = models.ForeignKey(
        'Realm', null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    image = CloudinaryField(
        'image', default='placeholder', asset_folder='/treasures/',
        use_filename=True, unique_filename=False
    )
    date_added = models.DateField(auto_now_add=True)
    unique_stock = models.BooleanField(default=False)

    # Serving a local dev_placeholder image when debug is on to prevent to
    # many cloudinary impressions when in testing.
    @property
    def image_url(self):
        if settings.DEBUG:
            return static('images/dev_placeholder.png')
        else:
            return self.image.url

    def __str__(self):
        return self.name

    def realm_name(self):
        return self.realm.name.replace('_', ' ')

    def clean(self):
        """
        validation to enforce a maximum stock limit for unique products
        """
        super().clean()
        if self.unique_stock and self.stock > 1:
            raise ValidationError(
                {'stock': 'Stock cannot exceed 1 for unique items.'}
                )
