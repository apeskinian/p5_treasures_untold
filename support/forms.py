from django import forms

from .models import ContactMessage, Faqs, FaqsTopics, Newsletter, Subscriber


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name', 'email', 'message'
        ]

    def __init__(self, *args, **kwargs):
        """
        Hides field labels, adds placeholders with asterisks for required
        fields, and sets focus on the `name` field.
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
        Hides label, adds placeholder and sets focus on the `reply`
        field.
        """
        super().__init__(*args, **kwargs)

        self.fields['reply'].widget.attrs['autofocus'] = True
        self.fields['reply'].widget.attrs['placeholder'] = 'Reply here...'
        self.fields['reply'].label = False


class FaqsTopicsForm(forms.ModelForm):
    class Meta:
        model = FaqsTopics
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        """
        Hides label and adds placeholder to `name` field.
        """
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Topic name...'
        self.fields['name'].label = False


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
        """
        Hides labels and adds placeholders to fields.

        Replaces the `topic` field with a `ChoiceField` containing:
        - An empty label ("- Select a Topic -") to prompt the user to choose a
            topic.
        - A "new" option ("Add New Topic") that allows users to create a new
            topic.
        """
        super().__init__(*args, **kwargs)

        self.fields['question'].widget.attrs['placeholder'] = 'Question'
        self.fields['answer'].widget.attrs['placeholder'] = 'Answer'
        self.fields['question'].label = False
        self.fields['answer'].label = False
        self.fields['topic'].label = False

        topic_choices = [
            (topic.id, topic.name) for topic in FaqsTopics.objects.all()
        ]
        self.fields['topic'].empty_label = "- Select a Topic -"
        self.fields['topic'] = forms.ChoiceField(
            choices=[
                ('', '- Select a Topic -'), ('new', 'Add New Topic')
            ] + topic_choices,
            required=True
        )

    def save(self, commit=True):
        """
        Overrides the form's save method to handle new topic creation.

        **Behavior:**
        - If there is a new topic, it is created and replaces the placholder
            topic that was set in the clean method.

        **Raises:**
        - Exception: If there is problem creating and assigning the new topic.

        **Returns:**
        - instance: The updated instance of :form:`support.FaqsTopicForm` with
            a new topic selected if one was created.
        """
        instance = super().save(commit=False)

        # Check for cleaned new topic data.
        new_topic_name = self.cleaned_data.get('new_topic', '').strip()

        # If a new topic exists, create the topic and assign it to the FAQ.
        if new_topic_name:
            try:
                topic_obj, created = (
                    FaqsTopics.objects.get_or_create(
                        name=new_topic_name
                    )
                )
                instance.topic = topic_obj
            except Exception as e:
                self.add_error('topic', f'An error occured: {str(e)}')

        if commit:
            instance.save()
        return instance

    def clean(self):
        """
        Overrides the form's clean method to handle topic selection, allowing
        the creation of a new topic if `Add New Topic` is chosen.

        **Behavior:**
        - If `Add New Topic` is selected, a placeholder topic is used to pass
         form validation so that a new topic can be created in the save method.
        - If an existing topic is selected, it is validated and assigned.

        **Raises:**
        - Error: If the new topic name is invalid.
        - Exception: If `Add New Topic` is selected but the topic placeholder
            fails.
        - `Topic.DoesNotExist`: If the selected existing topic does not exist.

        **Returns:**
        - dict: The cleaned data, with the `topic` field set to either the
            placeholder or selected topic instance.
        """
        # Set variables for method.
        cleaned_data = super().clean()
        topic = cleaned_data.get('topic')
        new_topic = cleaned_data.get('new_topic').strip()

        # If 'Add new topic' is selected check for invalid input first
        if topic == 'new' and not new_topic:
            self.add_error(
                'topic',
                'Topic cannot be blank.'
            )
        # If there is a valid new topic name, use an existing topic as a
        # placeholder first to pass form validation.
        elif topic == 'new':
            try:
                cleaned_data['topic'] = FaqsTopics.objects.first()
            except Exception as e:
                self.add_error(
                    'topic',
                    'An error occured while processing the new topic: '
                    f'{str(e)}'
                )
        # Otherwise process the chosen topic as normal
        else:
            try:
                cleaned_data['topic'] = FaqsTopics.objects.get(pk=int(topic))
            except FaqsTopics.DoesNotExist:
                self.add_error(
                    'topic',
                    'Invalid topic selected.'
                )

        return cleaned_data


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'news_body']

    def __init__(self, *args, **kwargs):
        """
        Hides labels and adds placeholders to fields.
        """
        super().__init__(*args, **kwargs)

        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['subject'].label = False
        self.fields['news_body'].widget.attrs['placeholder'] = '...'
        self.fields['news_body'].label = False


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

    def __init__(self, *args, **kwargs):
        """
        Hides label and adds placeholder to `email` field.
        """
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'email@example.com'
        self.fields['email'].label = False

    def validate_unique(self):
        """
        Override default unique validation to prevent automatic errors.
        Unique validation is handled in the view to present an info message
        rather then an error.
        """
        pass
