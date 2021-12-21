from django.contrib import admin
from .models import custom_user


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'username', 'purpose', 'belong')

admin.site.register(custom_user)