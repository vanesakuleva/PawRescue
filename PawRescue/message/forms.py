from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['recipient', 'sender', 'answered']

    def __init__(self, *args, **kwargs):
        original_subject = kwargs.pop('original_subject', None)
        if original_subject:
            initial_subject = f"Re: {original_subject}"
            kwargs.setdefault('initial', {})['subject'] = initial_subject
        super().__init__(*args, **kwargs)