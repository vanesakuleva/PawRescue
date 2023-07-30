from django import forms

from PawRescue.events.models import AdoptionEvent


class AdoptionEventForm(forms.ModelForm):
    class Meta:
        model = AdoptionEvent
        exclude = ['organizer', 'participant_count']

        widgets = {
            'photo': forms.FileInput()
            #da si donapisha widgets
        }
