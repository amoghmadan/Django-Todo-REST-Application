from rest_framework import serializers

from . import choices
from .models import Task


TaskStatusChoiceSerializer = type('TaskStatusChoiceSerializer', (serializers.Serializer, ), {
    key: serializers.CharField(default=value, read_only=True) for key, value in choices.TASK_STATUS_CHOICE
})


class TaskSerializer(serializers.ModelSerializer):
    """."""

    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        """."""

        model = Task
        exclude = ['user']
