from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from PawRescue.accounts.models import Profile

User = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': 'Password'
            }
        ),
        label='Password:')

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': 'Repeat password'
            }
        ),
        label='Repeat password:')

    class Meta:
        model = User
        fields = ['email', 'username']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Type your Email'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Type your username'
                }
            ),
        }


class LoginUserForm(auth_forms.AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password1']




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'profile_picture']


class ChangePasswordForm(auth_forms.PasswordChangeForm):
    pass
