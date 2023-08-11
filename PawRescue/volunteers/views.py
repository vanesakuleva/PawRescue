from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from PawRescue.volunteers.forms import VolunteerApplicationForm
from PawRescue.volunteers.models import VolunteerApplication


# Create your views here.
class VolunteerApplicationView(CreateView):
    model = VolunteerApplication
    template_name = 'volunteers/volunteer_application.html'
    form_class = VolunteerApplicationForm
    success_url = reverse_lazy('thank you')


class ThankYouView(TemplateView):
    template_name = 'volunteers/thank_you.html'


def approve_volunteer_view(request, pk):
    application = get_object_or_404(VolunteerApplication, pk=pk)

    if application.status == 'Pending':
        application.status = 'Accepted'
        application.save()
        messages.success(request, 'Volunteer application approved successfully.')
    else:
        messages.error(request, 'The volunteer application is already approved or rejected.')

    return redirect('admin:volunteers_volunteerapplication_changelist')
