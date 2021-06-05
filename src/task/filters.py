from django_filters import rest_framework as filters

from .models import Task


class TaskFilterSet(filters.FilterSet):
    """Filter Set for Task Model"""

    class Meta:
        """Making status filterable"""

        model = Task
        fields = {
            'status': ['exact'],
        }
