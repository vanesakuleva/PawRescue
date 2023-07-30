from django.contrib.auth import views
from django.views.generic.list import ListView

from PawRescue.events.models import AdoptionEvent
from PawRescue.pets.models import Pet


class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    context_object_name = 'user'


class PetsCatalogView(ListView):
    template_name = 'common/pet-posts.html'

    def get_queryset(self):
        return Pet.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.all()
        return context


class EventCatalogView(ListView):
    model = AdoptionEvent
    template_name = 'common/adoption_events.html'
    context_object_name = 'events'
