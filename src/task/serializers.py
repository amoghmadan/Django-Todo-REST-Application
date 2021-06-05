from rest_framework import serializers

from .choices import TaskStatus
from .models import Task

"""Task Status (choices) as a dictionary"""
TaskStatusChoiceSerializer = type("TaskStatusChoiceSerializer", (serializers.Serializer, ), {
    key: serializers.CharField(default=value, read_only=True) for key, value in TaskStatus.choices
})


class TaskSerializer(serializers.ModelSerializer):
    """Task Model Serializer"""

    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        """Excluding 'user' field for read and write"""

        model = Task
        exclude = ['user']
