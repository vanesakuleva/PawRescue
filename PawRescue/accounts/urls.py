from django.contrib import auth
from django.contrib.auth import views
from django.urls import path

from PawRescue.accounts.views import RegisterUserView, LoginUserView, LogoutUserView, DetailsUserView, UpdateUserView, \
    DeleteUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('<int:pk>/', DetailsUserView.as_view(), name='details user'),
    path('edit/', UpdateUserView.as_view(), name='edit user'),
    path('delete/', DeleteUserView.as_view(), name='delete user'),
]
