from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from PawRescue.events.forms import AdoptionEventForm


# Create your views here.
class AdoptionEventCreateView(generic.FormView):
    template_name = 'events/create_adoption_event.html'
    form_class = AdoptionEventForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        event = form.save(commit=False)

        selected_hashtags = form.cleaned_data.get('hashtags', [])
        custom_hashtags = form.cleaned_data.get('custom_hashtags', '')
        combined_hashtags = ','.join(selected_hashtags)
        if custom_hashtags:
            if combined_hashtags:
                combined_hashtags += f',{custom_hashtags}'
            else:
                combined_hashtags = custom_hashtags

        event.hashtags = combined_hashtags
        event.organizer = self.request.user
        event.save()

        return super().form_valid(form)
