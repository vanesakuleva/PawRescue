from django.shortcuts import render
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


class DeleteEventView(views.DeleteView):
    model = AdoptionEvent
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url

    def delete(self, request, *args, **kwargs):
        self.object.delete()
        return redirect(self.get_success_url())
