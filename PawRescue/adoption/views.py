from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from PawRescue.adoption.forms import AdoptionForm
from PawRescue.adoption.models import Adoption


class AdoptionDetailView(views.CreateView):
    model = Adoption
    form_class = AdoptionForm
    template_name = 'adoption/adoption_details.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        pet_id = self.kwargs['pk']
        form.instance.pet_id = pet_id
        form.instance.user = self.request.user
        form.instance.status = 'Pending'
        return super().form_valid(form)