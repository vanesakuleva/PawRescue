from django import forms

from PawRescue.adoption.models import Adoption


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        exclude = ['user', 'pet', 'adoption_date', 'is_completed']
