
from django.views import generic as views
from django.contrib.auth import views as auth_views,get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from PawRescue.accounts.forms import RegisterUserForm
from PawRescue.accounts.models import Profile

UserModel = get_user_model()


class PermissionMixin(views.View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(PermissionMixin, views.CreateView):
    template_name = 'user/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url


class LoginUserView(auth_views.LoginView):
    pass


class LogoutUserView(auth_views.LogoutView):
    pass


class DetailsUserView(views.DetailView):
    model = Profile
    template_name = 'user/details-account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        profile = Profile.objects.get(pk=user.id)
        context['profile'] = profile

        return context





class UpdateUserView(views.UpdateView):
    pass


class DeleteUserView(views.DeleteView):
    pass
