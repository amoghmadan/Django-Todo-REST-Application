from rest_framework import generics

from .serializers import TaskStatusChoiceSerializer


class TaskStatusChoiceView(generics.RetrieveAPIView):
    """Retrieve the Task Status (Choices) as JSON object"""

    serializer_class = TaskStatusChoiceSerializer

    def get_object(self):
        """Returning {} because default values are set in serializer"""

        return {}
