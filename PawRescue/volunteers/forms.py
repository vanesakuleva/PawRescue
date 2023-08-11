from django import forms

from PawRescue.volunteers.models import VolunteerApplication


class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = [
            'full_name',
            'email',
            'contact_number',
            'address',
            'skills',
            'availability',
            'why_volunteer',
        ]
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Type your full name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Type your Email'
                }
            ),
            'contact_number': forms.TextInput(
                attrs={
                    'placeholder': 'Type your phone number'
                }
            ),

            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Type your full address',
                }
            ),
            'skills': forms.TextInput(
                attrs={
                    'placeholder': 'Type your skills'
                }
            ),
            'availability': forms.TextInput(
                attrs={
                    'placeholder': 'Type your free hours'
                }
            ),
            'why_volunteer': forms.Textarea(
                attrs={
                    'placeholder': 'Tell us why you want to be a volunteer'
                }
            )

        }
