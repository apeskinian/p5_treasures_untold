import uuid
from django.utils import timezone
from django.db import models


class ContactMessage(models.Model):
    """
    Represents a customer support message submitted via the contact form.

    **Fields:**
    - `ticket_number (CharField)`: A unique identifier for the message,
      generated automatically if not provided.
    - `name (CharField)`: The name of the person submitting the message.
    - `email (EmailField)`: The email address of the sender.
    - `message (TextField)`: The content of the message.
    - `replied (BooleanField)`: A flag indicating whether the message has
      been replied to (default: `False`).
    - `date_received (DateField)`: The date when the message was received,
      automatically set upon creation.
    - `date_replied (DateField)`: The date when a reply was sent
      (optional, set when a reply is made).
    - `reply (TextField)`: The content of the reply (optional).

    **Meta:**
    - Messages are ordered by `replied` status, ensuring unreplied messages
      appear first.

    **Methods:**
    - `_generate_ticket_number()`: Generates a unique ticket number with a
      'TU' prefix and an 8-character hexadecimal string.
    - `save()`: Overrides the default save method to ensure a ticket number
      is assigned if not already present.
    - `__str__()`: Returns a string representation of the contact message,
      including the ticket number and sender's name.
    """
    class Meta:
        ordering = ['replied', ]

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
    """
    Represents a topic category for Frequently Asked Questions (FAQs).

    **Fields:**
    - `name (CharField)`: The name of the FAQ topic.
    - `sort_order (PositiveIntegerField)`: Determines the display order of
      topics (default: 100).

    **Meta:**
    - `verbose_name_plural`: Sets the plural name to 'FAQ Topics'.
    - `ordering`: Topics are ordered by `sort_order` in ascending order.

    **Methods:**
    - `__str__()`: Returns the topic name as its string representation.
    """
    class Meta:
        verbose_name_plural = 'FAQ Topics'
        ordering = ['sort_order', ]

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
    """
    Represents an individual Frequently Asked Question (FAQ).

    **Fields:**
    - `topic (ForeignKey)`: Links the FAQ to a specific `FaqsTopics` category.
    - `question (CharField)`: The FAQ question text.
    - `answer (TextField)`: The answer to the question.
    - `sort_order (PositiveIntegerField)`: Determines the display order of
      questions within a topic (default: 100).

    **Meta:**
    - `verbose_name_plural`: Sets the plural name to 'FAQs'.
    - `ordering`: FAQs are ordered by `topic` and `sort_order`.

    **Methods:**
    - `__str__()`: Returns the FAQ question as its string representation.
    """
    class Meta:
        verbose_name_plural = 'FAQs'
        ordering = ['topic', 'sort_order', ]

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
    """
    Represents a newsletter entry that has been sent.

    **Fields:**
    - `subject (CharField)`: The subject line of the newsletter.
    - `news_body (TextField)`: The main content of the newsletter.
    - `date_sent (DateField)`: The date the newsletter was sent
        (auto-populated).

    **Meta:**
    - `ordering`: Newsletters are ordered by `date_sent`.

    **Methods:**
    - `__str__()`: Returns the newsletter subject as its string representation.
    """
    class Meta:
        ordering = ['-date_sent']

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
    """
    Represents a newsletter subscriber.

    **Fields:**
    - `email (EmailField)`: The subscriber's email address (unique).
    - `is_active (BooleanField)`: Indicates whether the subscription is active.
    - `date_joined (DateField)`: The date the user subscribed (optional).
    - `token (CharField)`: A unique token for confirming or managing the
        subscription.
    - `token_created_at (DateTimeField)`: Timestamp for when the token was
        generated.

    **Meta:**
    - `ordering`: Subscribers are ordered by `date_joined`.

    **Methods:**
    - `__str__()`: Returns the subscriber's email as its string representation.
    """
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
