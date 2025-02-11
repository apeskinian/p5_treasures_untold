from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return self.name


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
