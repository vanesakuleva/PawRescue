from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views, generic

from PawRescue.adoption.forms import AdoptionForm
from PawRescue.adoption.models import Adoption, ApprovedAdoption


class AdoptionDetailView(generic.CreateView):
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


class ApproveAdoptionView(views.View):
    def get(self, request, adoption_id):
        # Get the adoption instance based on the provided adoption_id
        adoption = get_object_or_404(Adoption, id=adoption_id)

        # Check if the admin has approved the adoption
        if 'is_approved' in request.GET:
            adoption.status = 'Accepted'  # Set the status to 'Accepted'
            adoption.save()

            # Create an ApprovedAdoption entry for the approved adoption
            ApprovedAdoption.objects.create(adoption=adoption)

            # Redirect to the change page of the ApprovedAdoption model in the admin panel
            change_url = reverse(
                'admin:%s_%s_change' % (ApprovedAdoption._meta.app_label, ApprovedAdoption._meta.model_name),
                args=[adoption_id])
            return redirect(change_url)

        # Redirect back to the admin homepage if not approved
        return redirect(reverse('admin:index'))

    # For handling post requests as well (optional)
    def post(self, request, adoption_id):
        return self.get(request, adoption_id)


@login_required
def owner_approved_adoptions(request):
    user = request.user
    approved_adoptions = ApprovedAdoption.objects.filter(adoption__user=user)
    return render(request, 'adoption/owner_approved_adoptions.html', {'approved_adoptions': approved_adoptions})
