from django.contrib import admin
from .models import board


# Register your models here.

class Board_Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at',
                    'still_ing', 'dday', 'members', 'part',
                    'place', 'detail')

admin.site.register(board, Board_Admin)