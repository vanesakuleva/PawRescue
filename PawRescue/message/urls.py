from django.urls import path

from PawRescue.message.views import CreateMessageView, message_sent_success, inbox

urlpatterns = [
    path('create/<int:pk>/', CreateMessageView.as_view(), name='create_message'),
    path('sent_success/<str:recipient>/', message_sent_success, name='message_sent_success'),
    path('inbox/', inbox, name='inbox'),
    path('answer/<int:message_pk>/', CreateMessageView.as_view(), name='answer_message'),
]