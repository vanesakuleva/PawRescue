from django.views import generic as views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from PawRescue.pets.forms import PetForm
from PawRescue.pets.models import Pet


class CreatePetView(views.CreateView):
    template_name = 'posts/add-post.html'
    form_class = PetForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url


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
    fields = '__all__'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pet = self.object.pet
    #     return context


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
