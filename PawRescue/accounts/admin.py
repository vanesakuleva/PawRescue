from datetime import datetime
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Account, Profile

UserModel = get_user_model()


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_staff', 'is_superuser')
    list_filter = ('is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_log')

    def is_admin_display(self, obj):
        return obj.user.is_staff

    is_admin_display.short_description = 'Is Admin'
    is_admin_display.boolean = True


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'age', 'profile_picture', "years_of_experience")
    search_fields = ('user__email', 'user__username')

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = 'Full Name'

    def years_of_experience(self, obj):
        if obj.user.date_joined:
            current_year = datetime.now().year
            join_year = obj.user.date_joined.year
            experience_years = current_year - join_year
            return experience_years
        return None

    years_of_experience.short_description = 'Years of Experience'
