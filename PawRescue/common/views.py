from django.contrib.auth import views
from django.shortcuts import render

from PawRescue.pets.models import Pet


class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    context_object_name = 'user'


class PetsCatalog(views.TemplateView):
    template_name = 'common/pet-posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.all()
        return context
