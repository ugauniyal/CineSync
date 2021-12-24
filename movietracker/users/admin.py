from users.models import Profile
from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name = 'Profile'
#     verbose_name_plural = 'Profiles'

# class CustomizeUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

# admin.site.unregister(User)
# admin.site.register(User, CustomizeUserAdmin)

admin.site.register(Profile)