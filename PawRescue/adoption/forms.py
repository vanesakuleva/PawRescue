from django import forms

from PawRescue.adoption.models import Adoption


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        exclude = ['user', 'pet', 'adoption_date', 'is_completed', 'status', 'pet_owner', 'is_approved']
        widgets = {
            'contact_number': forms.TextInput(
                attrs={
                    'placeholder': 'Type your mobile phone'
                }
            ),
            'home_environment': forms.TextInput(
                attrs={
                    'placeholder': 'Please provide information about your home environment'
                }
            ),
            'previous_pet_experience': forms.TextInput(
                attrs={
                    'placeholder': 'Tell us about your previous experience with pets'
                }
            ),
            'reason_for_adoption': forms.TextInput(
                attrs={
                    'placeholder': 'Please let us know your reason for adopting a pet'
                }
            ),
        }
