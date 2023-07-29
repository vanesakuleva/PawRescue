from django import forms

from PawRescue.events.models import AdoptionEvent


class AdoptionEventForm(forms.ModelForm):
    HASHTAG_CHOICES = [
        ('adoptionfair', '#AdoptionFair'),
        ('petmeetup', '#PetMeetup'),
        ('fundraiser', '#Fundraiser'),
        ('petadoption', '#PetAdoption'),
        ('rescueevent', '#RescueEvent'),
        ('fosterawareness', '#FosterAwareness'),
        ('adoptdontshop', '#AdoptDontShop'),
        ('pawsomeevent', '#PawsomeEvent'),
        ('furryfriends', '#FurryFriends'),
        ('shelterfundraiser', '#ShelterFundraiser'),
        ('pethealthclinic', '#PetHealthClinic'),
        ('animalcharity', '#AnimalCharity'),
        ('petsocial', '#PetSocial'),
        ('adoptablepets', '#AdoptablePets'),
        ]
    hashtags = forms.MultipleChoiceField(
        choices=HASHTAG_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    custom_hashtags = forms.CharField(
        max_length=200,
        required=False,
        help_text='Enter custom hashtags separated by commas.'
    )

    def clean(self):
        cleaned_data = super().clean()
        selected_hashtags = cleaned_data.get('hashtags', [])
        custom_hashtags = cleaned_data.get('custom_hashtags', '').strip()

        if custom_hashtags:
            # Combine the selected choices with custom hashtags
            selected_hashtags += custom_hashtags.split(',')

        cleaned_data['hashtags'] = selected_hashtags
        return cleaned_data

    class Meta:
        model = AdoptionEvent
        fields = ['name', 'description', 'location', 'start_date', 'end_date', 'organizer', 'photo',
                  'participant_count', 'hashtags', 'custom_hashtags']