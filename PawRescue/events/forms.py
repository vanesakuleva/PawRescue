from django import forms

from PawRescue.events.models import AdoptionEvent
from PawRescue.pets.models import Pet

class DateTimeInput(forms.DateInput):
    input_type = 'date'

    def __int__(self, **kwargs):
        kwargs['format'] = "%d-%m-%Y"
        super().__init__(**kwargs)


class AdoptionEventForm(forms.ModelForm):
    class Meta:
        model = AdoptionEvent
        exclude = ['organizer', 'participant_count', 'participants']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Type the name of Event'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Type the description'
                }
            ),
            'location':forms.TextInput(
                attrs={
                    'placeholder': 'Type event location'
                }
            ),
            'start_date':DateTimeInput,
            'end_date':DateTimeInput


        }
