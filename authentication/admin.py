from django.contrib import admin
from .models import custom_user


# Register your models here.

class User_Admin(admin.ModelAdmin):
    list_display = ('username', 'nickname')

admin.site.register(custom_user, User_Admin)