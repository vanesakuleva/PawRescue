from django import forms

from PawRescue.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['created_by']
