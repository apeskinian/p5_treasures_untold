from django.db.models.signals import post_delete
from django.dispatch import receiver

from cloudinary.uploader import destroy

from .models import Product


@receiver(post_delete, sender=Product)
def delete_image_from_cloudinary(sender, instance, **kwargs):
    """
    Deletes the image from Cloudinary when a product is deleted, unless the
    image is a placeholder.

    **Arguments:**
    - `sender`: The model class that sent the signal.
    - `instance`: The instance of the product that was deleted.
    - `kwargs`: Additional keyword arguments passed with the signal.
    """
    if instance.image and instance.image.public_id != 'placeholder':
        public_id = instance.image.public_id
        destroy(public_id)
