from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class UserModelAdmin(UserAdmin):
  model = User
  list_display = ["id","email","username","is_superuser","is_staff"]
  list_filter = ["is_superuser"]
  fieldsets = [("User Credentials",{"fields": ["email", "password"]}),("Personal Information",{"fields":["username"]}),("Permissions",{"fields":["is_staff","is_superuser"]})]

  add_fieldsets = [
    (None, {
      "classes": ["wide"],
      "fields": ["email","password1", "password2"]
    })
  ]
  filter_horizontal = []

admin.site.register(User, UserModelAdmin)