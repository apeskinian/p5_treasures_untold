from django.db.models.signals import post_delete
from django.dispatch import receiver
from cloudinary.uploader import destroy
from .models import Product

@receiver(post_delete, sender=Product)
def delete_image_from_cloudinary(sender, instance, **kwargs):
    # making sure the image is not a placeholder and deleting image
    if instance.image and instance.image != 'placeholder':
        public_id = str(instance.image)
        destroy(public_id)