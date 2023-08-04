from django import forms

from PawRescue.events.models import AdoptionEvent
from PawRescue.pets.models import Pet


class AdoptionEventForm(forms.ModelForm):
    class Meta:
        model = AdoptionEvent
        exclude = ['organizer', 'participant_count', 'participants']

        widgets = {
            'photo': forms.FileInput()
            #da si donapisha widgets
        }
