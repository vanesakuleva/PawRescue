from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from PawRescue.events.models import AdoptionEvent
from PawRescue.pets.models import Pet


class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    context_object_name = 'user'


class PetsCatalogView(ListView):
    template_name = 'common/pet-posts.html'

    def get_queryset(self):
        return Pet.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.all().order_by('-created_at')
        return context


class EventCatalogView(ListView):
    model = AdoptionEvent
    template_name = 'common/adoption_events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return AdoptionEvent.objects.all().order_by('-created_at')


@login_required
def add_participant(request, event_id):
    event = get_object_or_404(AdoptionEvent, id=event_id)
    if request.user.is_authenticated:
        event.participants.add(request.user)
    return redirect('event catalog')


@login_required
def remove_participant(request, event_id):
    event = get_object_or_404(AdoptionEvent, id=event_id)
    if request.user.is_authenticated:
        event.participants.remove(request.user)
    return redirect('event catalog')
