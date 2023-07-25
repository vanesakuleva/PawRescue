from django.urls import path

from PawRescue.adoption.views import AdoptionDetailView, ApproveAdoptionView, \
    OwnerApprovedAdoptionsView, MoreInfo

urlpatterns = [
    path('new/<int:pk>/', AdoptionDetailView.as_view(), name='adoption form'),
    path('approve_adoption/<int:adoption_id>/', ApproveAdoptionView.as_view(), name='approve adoption'),
    path('profile/approved_adoptions/', OwnerApprovedAdoptionsView.as_view(), name='owner approved adoptions'),
    path('adoption/profile/approved_adoptions/more_info/<int:pk>/', MoreInfo.as_view(), name='more info'),
]

