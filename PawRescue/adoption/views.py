from django.shortcuts import render, get_object_or_404, redirect
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


class OwnerApprovedAdoptionsView(views.View):
    template_name = 'adoption/owner_approved_adoptions.html'

    def get(self, request):
        pet_pk = request.GET.get('pet_pk')
        pet = get_object_or_404(Pet, pk=pet_pk)
        pet_owner = pet.created_by

        if request.user == pet_owner:
            approved_adoptions = Adoption.objects.filter(pet_owner=pet_owner, status='Accepted')
            return render(request, self.template_name, {'approved_adoptions': approved_adoptions})

# owner_approved_adoptions = login_required(OwnerApprovedAdoptionsView.as_view())
