from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model

from PawRescue.accounts.models import Account, Profile
from django.contrib import admin
from .models import Profile, Account

UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)
    list_display = ('email', 'username', 'is_admin', 'is_staff', 'is_superuser')
    list_filter = ('is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_log')

    def get_full_name(self, obj):
        return obj.profile.get_full_name()

    get_full_name.short_description = 'Full Name'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'age', 'profile_picture')
    list_filter = ('age',)
    search_fields = ('first_name', 'last_name')

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = 'Full Name'

# @admin.register(Profile)
# class RegisterProfile(admin.ModelAdmin):
#     ordering = ['first_name', 'last_name', 'age']
#
#
# @admin.register(Account)
# class RegisterAuthUser(admin.ModelAdmin):
#     pass
