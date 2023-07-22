from django.contrib import admin

from PawRescue.adoption.models import Adoption


@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'status')
    list_filter = ('status',)
