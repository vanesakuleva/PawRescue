from django import views
from django.urls import path

from PawRescue.events.views import AdoptionEventCreateView, EventCatalogView

urlpatterns = [
    path('create/', AdoptionEventCreateView.as_view(), name='create adoption event'),
    path('events/catalog/', EventCatalogView.as_view(), name='event catalog'),
]
