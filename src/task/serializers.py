from rest_framework import serializers

from . import choices
from .models import Task


TaskStatusChoiceSerializer = type('TaskStatusChoiceSerializer', (serializers.Serializer, ), {
    key: serializers.CharField(default=value) for key, value in dict(choices.TASK_STATUS_CHOICE).items()
})


class TaskSerializer(serializers.ModelSerializer):
    """."""

    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        """."""

        model = Task
        exclude = ['user']
