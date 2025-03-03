import uuid
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from cloudinary.utils import cloudinary_url
from django.conf import settings
from django.templatetags.static import static
from django.db.models.functions import Lower


class Realm(models.Model):
    name = models.CharField(max_length=254)
    the_prefix_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def display_name(self):
        return self.name.replace('_', ' ')


class Product(models.Model):
    class Meta:
        ordering = [Lower('realm__name')]

    name = models.CharField(max_length=254)
    realm = models.ForeignKey(
        'Realm', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='product_realm'
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        unique=True,
        editable=False
    )
    image = CloudinaryField(
        'image', default='placeholder', asset_folder='/treasures/',
        use_filename=True, unique_filename=False
    )
    date_added = models.DateField(auto_now_add=True)
    unique_stock = models.BooleanField(default=False)

    def _generate_sku(self):
        """
        Generate an order number from the item details
        """
        name_part = []
        name_part_words = self.name.split(' ')
        for word in name_part_words:
            name_part.append(word[0].upper())
        name_part = ''.join(name_part)
        realm_part = []
        realm_part_words = self.realm.display_name().split(' ')
        for word in realm_part_words:
            realm_part.append(word[:3].upper())
        realm_part = ''.join(realm_part)
        unique = '-U' if self.unique_stock else ''
        uuid_part = uuid.uuid4().hex[:4].upper()
        sku = f'TU-{realm_part}-{name_part}{unique}-{uuid_part}'

        return sku

    # Serving a local dev_mode image when debug is on to prevent too
    # many cloudinary impressions when in testing.
    @property
    def image_url(self):
        if settings.DEBUG:
            if str(self.image) == 'placeholder':
                return static('images/dev_placeholder.png')
            else:
                return static(f'images/dev_mode/{self.sku}.png')
        else:
            if str(self.image) == 'placeholder':
                return static('images/placeholder.png')
            else:
                return cloudinary_url(
                    self.image.public_id,
                    secure=True,
                    fetch_format='auto',
                    quality='auto:best',
                    width=500,
                    height=500,
                    crop='fill'
                )[0]

    def save(self, *args, **kwargs):
        """
        set an sku if not already present
        """
        if not self.sku:
            self.sku = self._generate_sku()
        super().save(*args, **kwargs)

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
