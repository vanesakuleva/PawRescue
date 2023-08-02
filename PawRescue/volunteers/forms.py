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
            'why_volunteer': forms.Textarea(attrs={'rows': 5}),
        }