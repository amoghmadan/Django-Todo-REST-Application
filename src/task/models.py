from django.db import models
from django.contrib.auth.models import User

from . import choices


class Task(models.Model):
    """."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=choices.TASK_STATUS_CHOICE, default=choices.TODO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
