from django.urls import path

from PawRescue.common.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('cataloguePets/', views.catalogue, name='catalogue Pets'),
)