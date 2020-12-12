from django_filters import rest_framework as filters

from .models import Task


class TaskFilterSet(filters.FilterSet):
    """."""

    class Meta:
        """."""

        model = Task
        fields = {
            'status': ['exact'],
        }
