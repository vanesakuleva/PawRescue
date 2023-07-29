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

    def clean_hashtags(self):
        selected_hashtags = self.cleaned_data['hashtags']
        custom_hashtags = self.cleaned_data['custom_hashtags']

        if custom_hashtags:
            # Combine the selected choices with custom hashtags
            selected_hashtags += custom_hashtags.split(',')

        return selected_hashtags

    class Meta:
        model = AdoptionEvent
        fields = ['name', 'description', 'location', 'start_date', 'end_date', 'organizer', 'image', 'participant_count', 'hashtags']