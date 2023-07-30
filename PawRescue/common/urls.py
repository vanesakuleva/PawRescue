from django.urls import path

from PawRescue.common import views
from PawRescue.common.views import IndexView, PetsCatalogView, EventCatalogView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('pet_catalog/', PetsCatalogView.as_view(), name='pet catalog'),
    path('event_catalog/', EventCatalogView.as_view(), name='event catalog'),

)
