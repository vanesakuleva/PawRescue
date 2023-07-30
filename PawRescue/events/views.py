from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from PawRescue.events.forms import AdoptionEventForm
from PawRescue.events.models import Hashtag


# Create your views here.
class AdoptionEventCreateView(generic.FormView):
    template_name = 'events/create_adoption_event.html'
    form_class = AdoptionEventForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        event = form.save(commit=False)

        # Save the event first to get its ID
        event.organizer = self.request.user
        event.save()

        selected_hashtags = form.cleaned_data.get('hashtags', [])
        custom_hashtags = form.cleaned_data.get('custom_hashtags', '').strip()

        # Create and add the selected hashtags
        for hashtag_name in selected_hashtags:
            hashtag, _ = Hashtag.objects.get_or_create(name=hashtag_name)
            event.hashtags.add(hashtag)

        # Create and add the custom hashtags
        if custom_hashtags:
            custom_hashtag_list = [tag.strip() for tag in custom_hashtags.split(',')]
            for custom_hashtag_name in custom_hashtag_list:
                custom_hashtag, _ = Hashtag.objects.get_or_create(name=custom_hashtag_name)
                event.hashtags.add(custom_hashtag)

        return super().form_valid(form)