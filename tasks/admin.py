from django.contrib import admin
from .models import task

@admin.register(task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Completed', 'Due_date', 'Created_at', 'Updated_at')
    list_filter = ('Completed', 'Due_date')
    search_fields = ('Title', 'Description')