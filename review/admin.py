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

class AuthorAdmin(admin.ModelAdmin):
  # model  = Author
  # list_display=['author_name']
  search_fields=['author_name']

class BookModelAdmin(admin.ModelAdmin):
  model = Book
  list_display = ['book_name']
  # search_fields=['author_name']
  autocomplete_fields = ['author']

admin.site.register(Genre)
admin.site.register(User, UserModelAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book, BookModelAdmin)
