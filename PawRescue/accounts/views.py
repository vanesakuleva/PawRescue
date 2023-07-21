from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from PawRescue.accounts.forms import RegisterUserForm, LoginUserForm, ProfileForm, ChangePasswordForm
from PawRescue.accounts.models import Profile, Account

UserModel = get_user_model()


class PermissionMixin(views.View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)


class SuccessURLMixin:
    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url


class RegisterUserView(PermissionMixin, SuccessURLMixin, views.CreateView):
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


class LoginUserView(SuccessURLMixin, auth_views.LoginView):
    template_name = 'user/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('index')


class LogoutConfirmationView(views.TemplateView):
    template_name = 'user/logout.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


def logout_user(request):
    logout(request)
    return redirect('index')


class DetailsUserView(views.DetailView):
    model = Profile
    template_name = 'user/details-account.html'
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        profile = Profile.objects.get(pk=user.id)
        context['profile'] = profile

        return context


class UpdateUserView(views.UpdateView):
    model = Profile
    template_name = 'user/edit-account.html'
    fields = ['first_name', 'last_name', 'age', 'profile_picture']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        profile = Profile.objects.get(pk=user.id)
        context['profile'] = profile
        return context

    def get_success_url(self):
        pk = self.object.pk
        return reverse('details user', kwargs={'pk': pk})


class DeleteUserView(views.DeleteView):
    model = Account
    template_name = 'user/delete-account.html'
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        self.object.delete()
        return redirect(self.get_success_url())


class ChangePasswordView(PermissionMixin, views.UpdateView):
    template_name = 'user/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('login user')  # Replace with the correct URL name.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'Change Password'
        return context

    def form_valid(self, form):
        form.save()
        # Logout the user after the password change.
        self.request.user.refresh_from_db()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs.pop('instance', None)
        return kwargs
