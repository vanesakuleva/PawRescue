from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from PawRescue.accounts.models import Profile

User = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']


class LoginUserForm(auth_forms.UserCreationForm):
    pass
