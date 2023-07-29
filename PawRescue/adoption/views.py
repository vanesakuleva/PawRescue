from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views, generic

from PawRescue.adoption.forms import AdoptionForm
from PawRescue.adoption.models import Adoption, ApprovedAdoption
from PawRescue.pets.models import Pet


class AdoptionDetailView(generic.CreateView):
    model = Adoption
    form_class = AdoptionForm
    template_name = 'adoption/adoption_details.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        pet_id = self.kwargs['pk']
        pet = get_object_or_404(Pet, id=pet_id)
        form.instance.pet_id = pet.pk
        form.instance.user = self.request.user
        form.instance.pet_owner = pet.created_by
        form.instance.status = 'Pending'
        return super().form_valid(form)


class ApproveAdoptionView(views.View):
    def get(self, request, adoption_id):
        adoption = get_object_or_404(Adoption, id=adoption_id)

        if 'is_approved' in request.GET:
            adoption.status = 'Accepted'
            adoption.save()
            ApprovedAdoption.objects.create(adoption=adoption)
            change_url = reverse(
                'admin:%s_%s_change' % (ApprovedAdoption._meta.app_label, ApprovedAdoption._meta.model_name),
                args=[adoption_id])
            return redirect(change_url)

        return redirect(reverse('admin:index'))

    def post(self, request, adoption_id):
        return self.get(request, adoption_id)


def get_approved_adoptions_for_user(user):
    pets_owned_by_user = Pet.objects.filter(created_by=user)
    return Adoption.objects.filter(pet__in=pets_owned_by_user, status='Accepted')


class OwnerApprovedAdoptionsView(LoginRequiredMixin, views.ListView):
    template_name = 'adoption/owner_approved_adoptions.html'
    context_object_name = 'approved_adoptions'

    def get_queryset(self):
        return get_approved_adoptions_for_user(self.request.user)


class MoreInfo(LoginRequiredMixin, views.DetailView):
    model = Adoption
    template_name = 'adoption/adoption_application_detail.html'
    context_object_name = 'adoption'


class MyApprovedAdoptionsView(LoginRequiredMixin, generic.ListView):
    template_name = 'adoption/my_adoption_application.html'
    context_object_name = 'my_approved_adoptions'
    model = Adoption

    def get_queryset(self):
        user = self.request.user
        return Adoption.objects.filter(user=user)
