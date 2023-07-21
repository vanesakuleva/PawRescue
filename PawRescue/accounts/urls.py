from django.contrib import auth
from django.contrib.auth import views
from django.urls import path

from PawRescue.accounts.views import RegisterUserView, LoginUserView, LogoutConfirmationView, DetailsUserView, \
    UpdateUserView, \
    DeleteUserView, logout_user, ChangePasswordView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutConfirmationView.as_view(), name='logout'),
    path('logout/confirm/', logout_user, name='logout_confirm'),
    path('<int:pk>/', DetailsUserView.as_view(), name='details user'),
    path('<int:pk>/edit/', UpdateUserView.as_view(), name='edit user'),
    path('<int:pk>/delete/', DeleteUserView.as_view(), name='delete user'),
    path('<int:pk>/changePassword/', ChangePasswordView.as_view(), name='change password'),
]

