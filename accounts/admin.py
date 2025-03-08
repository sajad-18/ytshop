from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'full_name', 'is_admin')
    list_filter = ('is_admin', 'is_active')

    fieldsets = (
        ('Main', {'fields': ('full_name', 'phone_number', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )

    add_fieldsets = (
        ('Create User', {'fields': ('phone_number', 'email', 'full_name', 'password1', 'password2')}),
    )

    search_fields = ('full_name', 'phone_number')
    ordering = ('full_name', 'email')
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)


