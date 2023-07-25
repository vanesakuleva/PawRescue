from django.urls import path

from PawRescue.adoption.views import AdoptionDetailView, ApproveAdoptionView, \
    OwnerApprovedAdoptionsView

urlpatterns = [
    path('new/<int:pk>/', AdoptionDetailView.as_view(), name='adoption form'),
    path('approve_adoption/<int:adoption_id>/', ApproveAdoptionView.as_view(), name='approve_adoption'),
    path('profile/approved_adoptions/', OwnerApprovedAdoptionsView.as_view(), name='owner_approved_adoptions')
 ]
