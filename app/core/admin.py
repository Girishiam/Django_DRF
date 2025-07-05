from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _










class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    
    ordering = ['id']
    list_display = ['email', 'name', 'is_active', 'is_staff']
    list_filter = ['is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ['email', 'name']
    filter_horizontal = ['groups', 'user_permissions']
    list_per_page = 20  
    readonly_fields = ['last_login']
admin.site.register(models.User, UserAdmin)