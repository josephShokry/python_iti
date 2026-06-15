from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'views', 'created_at')
    list_filter = ('rate',)
    search_fields = ('title', 'description')
    readonly_fields = ('views', 'created_at')
    ordering = ('-created_at',)