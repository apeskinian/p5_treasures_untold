from django import forms
from .models import ContactMessage, Faqs, FaqsTopics, Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name', 'email', 'message'
        ]

    def __init__(self, *args, **kwargs):
        """
        add placeholders, remove auto-generated labels and set
        autofocus  on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email',
            'message': 'Type your message here...'
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class ContactReplyForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'reply',
        ]

    def __init__(self, *args, **kwargs):
        """
        add placeholders, remove auto-generated labels and set
        autofocus  on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['reply'].widget.attrs['autofocus'] = True
        self.fields['reply'].widget.attrs['placeholder'] = 'Reply here...'
        self.fields['reply'].label = False


class FaqsForm(forms.ModelForm):
    class Meta:
        model = Faqs
        fields = ['topic', 'question', 'answer']

    new_topic = forms.CharField(
        label=False,
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter new topic'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['question'].widget.attrs['placeholder'] = 'Question'
        self.fields['answer'].widget.attrs['placeholder'] = 'Answer'
        self.fields['question'].label = False
        self.fields['answer'].label = False

        topic_choices = [
            (topic.id, topic.name) for topic in FaqsTopics.objects.all()
        ]
        self.fields['topic'].empty_label = "- Select a Topic -"
        self.fields['topic'].label = False
        self.fields['topic'] = forms.ChoiceField(
            choices=[
                ('', '-- Select a Topic --'), ('new', 'Add New Topic')
            ] + topic_choices,
            required=True
        )

    def clean(self):
        cleaned_data = super().clean()
        topic = cleaned_data.get('topic')
        new_topic = cleaned_data.get('new_topic')

        if topic == "new":
            if not new_topic:
                self.add_error('new_topic', "Please enter a new topic.")
            else:
                topic_obj, created = (
                    FaqsTopics.objects.get_or_create(name=new_topic)
                )
                cleaned_data['topic'] = topic_obj
        else:
            try:
                cleaned_data['topic'] = FaqsTopics.objects.get(pk=int(topic))
            except FaqsTopics.DoesNotExist:
                self.add_error('topic', "Invalid topic selected.")

        return cleaned_data


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'email@example.com'
        self.fields['email'].label = False
