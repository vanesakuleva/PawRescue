from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from PawRescue.adoption.models import Adoption, ApprovedAdoption


@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'status', 'approve_button')
    list_filter = ('status',)

    def approve_button(self, obj):
        if obj.status == 'Pending':
            approve_url = reverse('approve_adoption', args=[obj.id]) + '?is_approved=true'
            return format_html('<a class="button" href="{}">Approve</a>', approve_url)
        return '-'

    approve_button.short_description = 'Approve'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if '_approve' in request.POST:
            adoption = self.get_object(request, object_id)

            if adoption and adoption.status == 'Pending' and not ApprovedAdoption.objects.filter(
                    adoption=adoption).exists():
                adoption.status = 'Accepted'
                adoption.save()
                ApprovedAdoption.objects.create(adoption=adoption)
                self.message_user(request, 'Adoption application approved successfully.', level='success')
                return HttpResponseRedirect(request.path_info)

        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(ApprovedAdoption)
class ApprovedAdoptionAdmin(admin.ModelAdmin):
    list_display = ('adoption', 'approval_date')
    list_filter = ('approval_date',)
