from django.urls import path

from PawRescue.events.views import AdoptionEventCreateView, DeleteEventView, UpdateEventView

urlpatterns = [
    path('create/', AdoptionEventCreateView.as_view(), name='create adoption event'),
    path('<int:pk>/edit/', UpdateEventView.as_view(), name='edit event'),
    path('<int:pk>/delete/', DeleteEventView.as_view(), name='delete event')

]
