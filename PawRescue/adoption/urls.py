from django.urls import path

from PawRescue.adoption.views import AdoptionDetailView

urlpatterns = [
    path('new/<int:pk>/', AdoptionDetailView.as_view(), name='adoption form'),
    # path('adoption/admin-approval/', AdminApprovalView.as_view(), name='admin_approval view'),
    # path('adoption/approve/', ApprovalLogicView.as_view(approval_status='approve'), name='approve adoption'),
    # path('adoption/reject/', ApprovalLogicView.as_view(approval_status='reject'), name='reject adoption'),
    # path('adoption/successful/', AdoptionSuccessfulView.as_view(), name='adoption successful view'),
 ]
