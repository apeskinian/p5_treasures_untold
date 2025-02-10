from django.db import models


class contactMessage(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return self.name
