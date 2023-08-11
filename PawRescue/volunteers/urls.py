from django.urls import path

from PawRescue.volunteers.views import VolunteerApplicationView, ThankYouView, approve_volunteer_view

urlpatterns = [
    path('volunteer_application/', VolunteerApplicationView.as_view(), name='volunteer application'),
    path('thank_you/', ThankYouView.as_view(), name='thank you'),
    path('approve_volunteer/<int:pk>/', approve_volunteer_view, name='approve_volunteer'),
]

