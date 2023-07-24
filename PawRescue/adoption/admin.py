from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from PawRescue.adoption.models import Adoption, ApprovedAdoption


@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'status', 'approve_button')

    def approve_button(self, obj):
        if obj.status == 'Pending':
            # Generate the URL for the approve_adoption view and add the is_approved parameter
            approve_url = reverse('approve_adoption', args=[obj.id]) + '?is_approved=true'
            return format_html('<a class="button" href="{}">Approve</a>', approve_url)
        return '-'

    approve_button.short_description = 'Approve Adoption'
