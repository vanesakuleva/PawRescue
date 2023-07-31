from django import forms

from PawRescue.events.models import AdoptionEvent
from PawRescue.pets.models import Pet


class AdoptionEventForm(forms.ModelForm):
    selected_pets = forms.ModelMultipleChoiceField(
        queryset=Pet.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = AdoptionEvent
        exclude = ['organizer', 'participant_count']

        widgets = {
            'photo': forms.FileInput()
            #da si donapisha widgets
        }
