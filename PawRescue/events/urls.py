from django import views
from django.urls import path

from PawRescue.events.views import AdoptionEventCreateView

urlpatterns = [
    path('create/', AdoptionEventCreateView.as_view(), name='create adoption event')
]
