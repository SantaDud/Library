from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomAdmin(UserAdmin):
    fieldsets = (
        ('Personal Info', {
            'classes':('collapse',),
            'fields' : ('username', 'first_name', 'last_name', 'password')
            }),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser')
            }),
        ('Details', {
            'fields': ('favorites', 'fine')
            }),
    )

admin.site.register(User, CustomAdmin)