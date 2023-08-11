from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from .models import VolunteerApplication


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'applied_date', 'status', 'approve_button')
    list_filter = ('applied_date', 'status')

    def approve_button(self, obj):
        if obj.status == 'Pending':
            approve_url = reverse('approve_volunteer', args=[obj.id]) + '?is_approved=true'
            return format_html('<a class="button" href="{}">Approve</a>', approve_url)
        return '-'

    approve_button.short_description = 'Approve'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if '_approve' in request.POST:
            application = self.get_object(request, object_id)

            if application and application.status == 'Pending':
                application.status = 'Accepted'
                application.save()
                self.message_user(request, 'Volunteer application approved successfully.', level='success')
                return HttpResponseRedirect(request.path_info)

        return super().change_view(request, object_id, form_url, extra_context)