from django.contrib import admin
from .models import Puzzle

@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'asked_in', 'solved')
    list_filter = ('category', 'solved')
    search_fields = ('title', 'asked_in')
    list_editable = ('solved',) 