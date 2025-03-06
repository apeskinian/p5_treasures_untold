import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.functions import Lower
from django.templatetags.static import static

from cloudinary.models import CloudinaryField
from cloudinary.utils import cloudinary_url


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
        Generates a unique SKU (Stock Keeping Unit) using UUID and product
        data.

        **Format:**
        `TU-REALM-PRODUCT-UNIQUE-XXXX`

        **Components:**
        - **REALM**: The first three letters of each word in the realm's
            display name (capitalized).
        - **PRODUCT**: The first letter of each word in the product name
            (capitalized).
        - **UNIQUE**: `U` if the product is unique, omitted otherwise.
        - **XXXX**: A 4-character uppercase hexadecimal string derived from a
            UUID.

        **Returns:**
        - A string representing the generated SKU.
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

    @property
    def image_url(self):
        """
        Returns the appropriate image URL for the instance based on the app's
        debug mode. This reduces the amount of impressions when testing.

        **Behavior:**
        - **Debug Mode (ON)**:
        - If the image is `placeholder`, returns a local static placeholder
            image.
        - Otherwise, returns a local static image using the SKU.
        - **Debug Mode (OFF)**:
        - If the image is `placeholder`, returns a generic static placeholder.
        - Otherwise, returns the Cloudinary-hosted image with optimized
            settings.

        **Returns:**
        - A static image URL if debug mode is enabled or if the image is a
            placeholder.
        - A Cloudinary URL if debug mode is disabled and the image is not a
            placeholder.
        """
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
        Assigns an SKU before saving if one is not already present.

        **Behavior:**
        - If the instance does not have an SKU, generates one using
            `_generate_sku()`.
        - Calls the parent `save` method to complete the save operation.

        **Returns:**
        - Saves the instance with an assigned SKU if missing.
        """
        if not self.sku:
            self.sku = self._generate_sku()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the `name` field as a string.

        **Returns:**
        - The `name` field as a string.
        """
        return self.name

    def realm_name(self):
        """
        Returns the `realm.name` field as a string with underscores replaced
        with spaces.

        **Returns:**
        - The `realm.name` field as a string with underscores replaced
        with spaces.
        """
        return self.realm.name.replace('_', ' ')

    def clean(self):
        """
        Override the clean method to enforce stock level validation for unique
        items.

        **Validation:**
        - If the item is marked as unique (`unique_stock = True`) and the stock
        level is adjusted to exceed 1, a `ValidationError` is raised.

        **Raises:**
        - `ValidationError`: If stock exceeds the allowed limit for unique
        items (i.e., stock > 1 when `unique_stock = True`).
        """
        super().clean()
        if self.unique_stock and self.stock > 1:
            raise ValidationError(
                {'stock': 'Stock cannot exceed 1 for unique items.'}
                )
