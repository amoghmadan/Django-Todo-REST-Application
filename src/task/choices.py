from django.db import models
from django.utils.translation import gettext_lazy as _


class TaskStatus(models.TextChoices):
    """Types of Task Status"""

    TODO = "todo", _("Todo")
    WIP = "wip", _("Work in Progress")
    ON_HOLD = "on_hold", _("On Hold")
    DONE = "done", _("Done")
