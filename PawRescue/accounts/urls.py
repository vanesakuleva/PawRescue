from django.urls import path

from PawRescue.accounts.views import login_user, register_user, details_user, edit_user, delete_user

urlpatterns = [
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    path('',details_user, name='details user'),
    path('edit/', edit_user, name='edit user'),
    path('delete/', delete_user, name='delete user'),
    ]


# urlpatterns = (
#     path('create/', views.ProfileCreateView.as_view(), name='create profile'),
#     path('login/', views.CustomLoginView.as_view(template_name='profiles/login.html'), name='login'),
#     path('logout/', views.CustomLogoutView.as_view(), name='logout'),
#     path('', views.UserDetailsView.as_view(), name='details profile'),
#     path('edit/', views.ProfileEditView.as_view(), name='edit profile'),
#     path('delete/', views.ProfileDeleteView.as_view(), name='delete profile')
# )