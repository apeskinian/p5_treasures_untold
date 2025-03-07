import uuid
from django.utils import timezone
from django.db import models


class ContactMessage(models.Model):
    class Meta:
        ordering = ['replied',]

    ticket_number = models.CharField(max_length=32, null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    replied = models.BooleanField(default=False)
    date_received = models.DateField(auto_now_add=True)
    date_replied = models.DateField(null=True, blank=True)
    reply = models.TextField(null=True, blank=True)

    def _generate_ticket_number(self):
        """
        Generate a unique ticket number using UUID with a 'TU' prefix.

        **Returns:**
        - A string in the format 'TU-XXXXXXXX', where:
        - 'XXXXXXXX' is an 8-character uppercase hex from a UUID.
        """
        return f'TU-{uuid.uuid4().hex[:8].upper()}'

    def save(self, *args, **kwargs):
        """
        Overides the standard save method by checking for a ticket number and
        generating one if not present.
        """
        if not self.ticket_number:
            self.ticket_number = self._generate_ticket_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the `ticket_number` and `name` fields as an f string.

        **Returns:**
        - The `ticket_number` and `name` fields as an f string.
        """
        return f'{self.ticket_number} - {self.name}'


class FaqsTopics(models.Model):
    class Meta:
        verbose_name_plural = 'FAQ Topics'
        ordering = ['sort_order',]

    name = models.CharField(max_length=100, null=False, blank=False)
    sort_order = models.PositiveIntegerField(default=100)

    def __str__(self):
        """
        Returns the `name` field as a string.

        **Returns:**
        - The `name` field as a string.
        """
        return self.name


class Faqs(models.Model):
    class Meta:
        verbose_name_plural = 'FAQs'
        ordering = ['topic', 'sort_order',]

    topic = models.ForeignKey(
        FaqsTopics, on_delete=models.CASCADE, related_name='faq_topic'
    )
    question = models.CharField(max_length=254, null=False, blank=False)
    answer = models.TextField()
    sort_order = models.PositiveIntegerField(default=100)

    def __str__(self):
        """
        Returns the `question` field as a string.

        **Returns:**
        - The `question` field as a string.
        """
        return self.question


class Newsletter(models.Model):
    class Meta:
        ordering = ['date_sent']

    subject = models.CharField(max_length=254, null=False, blank=False)
    news_body = models.TextField()
    date_sent = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        Returns the `subject` field as a string.

        **Returns:**
        - The `subject` field as a string.
        """
        return self.subject


class Subscriber(models.Model):
    class Meta:
        ordering = ['date_joined']

    email = models.EmailField(null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateField(null=True, blank=True)
    token = models.CharField(max_length=255)
    token_created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """
        Returns the `email` field as a string.

        **Returns:**
        - The `email` field as a string.
        """
        return self.email
