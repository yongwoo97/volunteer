from django.contrib import admin
from .models import board


# Register your models here.

class Board_Admin(admin.ModelAdmin):
    list_display = [field.name for field in board._meta.get_fields()]

admin.site.register(board, Board_Admin)