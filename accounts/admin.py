from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'email', 'username', 'first_name', 'last_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rasm',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('rasm',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)