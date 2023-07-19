from django.urls import path

from PawRescue.pets.views import CreatePetView, DetailsPetView, UpdatePetView, DeletePetView

urlpatterns = [
    path('register/', CreatePetView.as_view(), name='add pet'),
    path('<int:pk>/', DetailsPetView.as_view(), name='details pet'),
    path('<int:pk>/edit/', UpdatePetView.as_view(), name='edit pet'),
    path('<int:pk>/delete/', DeletePetView.as_view(), name='delete pet')]
