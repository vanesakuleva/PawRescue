from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from PawRescue.events.forms import AdoptionEventForm
from PawRescue.events.models import AdoptionEvent


class AdoptionEventCreateView(views.FormView):
    template_name = 'events/create_adoption_event.html'
    form_class = AdoptionEventForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        event = form.save(commit=False)
        event.organizer = self.request.user
        event.save()
        return super().form_valid(form)


class UpdateEventView(views.UpdateView):
    model = AdoptionEvent
    form_class = AdoptionEventForm
    template_name = 'events/edit-event.html'
    success_url = reverse_lazy('event catalog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.object
        context['event'] = event
        return context

    def form_valid(self, form):
        event = form.save(commit=False)
        event.organizer = self.request.user
        event.save()
        return super().form_valid(form)


class DeleteEventView(views.DeleteView):
    model = AdoptionEvent
    template_name = 'events/delete-event.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url

    def delete(self, request, *args, **kwargs):
        self.object.delete()
        return redirect(self.get_success_url())
