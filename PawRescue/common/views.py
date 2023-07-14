from django.contrib.auth import views
from django.shortcuts import render


# Create your views here.

class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    context_object_name = 'user'
