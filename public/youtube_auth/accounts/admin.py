from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Profile

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')
    search_fields = ['username', 'email']
    ordering = ['username']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']