from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.uploader import upload
from .models import Product

@receiver(post_save, sender=Product)
def upload_images_to_cloudinary(sender, instance, **kwargs):
    if instance.image and not instance.image.url.startswith('http'):
        # Local image file path
        local_path = f"fixtures/images/{instance.image}"
        # Upload to Cloudinary
        result = upload(local_path, folder='treasures')
        # Update instance with Cloudinary URL
        instance.image = result['public_id']
        instance.save()