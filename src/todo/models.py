from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """."""

    TODO = 'todo'
    DONE = 'done'
    HOLD = 'hold'

    STATUS_CHOICES = [
        (TODO, 'Todo'),
        (DONE, 'Done'),
        (HOLD, 'Hold'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=TODO)
    created_at = models.DateTimeField(auto_now_add=True)
