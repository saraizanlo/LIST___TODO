import django_filters
from .models import task

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Search by title')
    description = django_filters.CharFilter(lookup_expr='icontains', label='Search by description')
    due_date = django_filters.DateFromToRangeFilter(field_name='due_date', label='Due date range')
    created_at = django_filters.DateFromToRangeFilter(field_name='created_at', label='Created date range')

    class Meta:
        model = task
        fields = ['title', 'description', 'due_date', 'created_at']
