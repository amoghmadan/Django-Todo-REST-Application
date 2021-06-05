from django.db import models
from django.contrib.auth.models import User

from .choices import TaskStatus


class Task(models.Model):
    """Model to store task information"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=TaskStatus.choices, default=TaskStatus.TODO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
