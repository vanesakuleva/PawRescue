from django.urls import path

from PawRescue.common import views
from PawRescue.common.views import IndexView, PetsCatalog

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('pet_catalog/', PetsCatalog.as_view(), name='pet_catalog'),

)
