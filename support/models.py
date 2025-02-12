import uuid

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
        generates a ticket number using UUID and TU- in front
        """
        return f'TU-{uuid.uuid4().hex[:8].upper()}'

    def save(self, *args, **kwargs):
        """
        set a ticket number
        """
        self.ticket_number = self._generate_ticket_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.ticket_number} - {self.name}'


class FaqsTopics(models.Model):
    class Meta:
        verbose_name_plural = 'FAQ Topics'
        ordering = ['sort_order',]

    name = models.CharField(max_length=100, null=False, blank=False)
    sort_order = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name


class Faqs(models.Model):
    class Meta:
        verbose_name_plural = 'FAQs'
        ordering = ['topic', 'sort_order',]

    topic = models.ForeignKey(FaqsTopics, on_delete=models.CASCADE)
    question = models.CharField(max_length=254, null=False, blank=False)
    answer = models.TextField()
    sort_order = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.question
