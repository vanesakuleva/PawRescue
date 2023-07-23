from django.urls import path

from PawRescue.message.views import CreateMessageView, message_sent_success

urlpatterns = [
    path('create/', CreateMessageView.as_view(), name='inbox'),
    path('/sent_success/<str:recipient>/', message_sent_success, name='message_sent_success'),
]
