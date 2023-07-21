from django.views import generic as views
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from PawRescue.pets.forms import PetForm
from PawRescue.pets.models import Pet


class CreatePetView(views.CreateView):
    template_name = 'posts/add-post.html'
    form_class = PetForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            form.instance.created_by = self.request.user
            return super().form_valid(form)


class DetailsPetView(views.DetailView):
    model = Pet
    template_name = 'posts/post-details.html'
    form_class = PetForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pet = self.object.pet
    #     return context


class UpdatePetView(views.UpdateView):
    model = Pet
    template_name = 'posts/edit-post.html'
    exclude = ['created_by']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.created_by
        pet = Pet.objects.get(pk=user.id)
        context['pet'] = pet
        return context

    def get_success_url(self):
        pk = self.object.pk
        return reverse('details pet', kwargs={'pk': pk})

class DeletePetView(views.DeleteView):
    model = Pet
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url

    def delete(self, request, *args, **kwargs):
        self.object.delete()
        return redirect(self.get_success_url())
