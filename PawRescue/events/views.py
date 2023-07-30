from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from PawRescue.events.forms import AdoptionEventForm
from PawRescue.events.models import AdoptionEvent


class AdoptionEventCreateView(generic.FormView):
    template_name = 'events/create_adoption_event.html'
    form_class = AdoptionEventForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        event = form.save(commit=False)
        event.organizer = self.request.user
        event.save()
        return super().form_valid(form)


class EventCatalogView(generic.ListView):
    model = AdoptionEvent
    template_name = 'events/adoption_events.html'
    context_object_name = 'events'
