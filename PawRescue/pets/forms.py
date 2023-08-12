from django import forms

from PawRescue.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['created_by', " created_at"]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Type name of the pet'
                }
            ),
            'other_pet_type': forms.TextInput(
                attrs={
                    'placeholder': 'Other type? '
                }
            ),
            'breed': forms.TextInput(
                attrs={
                    'placeholder': 'Type the breed if have any'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Type the age of the pet'
                }
            ),
            'specifics_in_behavior': forms.Textarea(
                attrs={
                    'placeholder': 'Type specifics behavior if have any'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Type description'
                }
            ),
            'town': forms.TextInput(
                attrs={
                    'placeholder': 'Type the town were is the pet'
                }
            ),

        }
