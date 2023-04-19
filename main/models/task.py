from django.db import models
from .user import User
from .tag import Tag


class Task(models.Model):
    """
    Model representing a task to be completed.

    Attributes:
        name (str): The name of the task.
        description (str): The description of the task.
        created_date (datetime): The date and time the task was created.
        updated_date (datetime): The date and time the task was last updated.
        deadline (datetime): The deadline for completing the task.
        status (str): The current status of the task.
        priority (int): The priority of the task.
    """

    class Statuses(models.TextChoices):
        NEW_TASK = "new_task"
        IN_DEVELOPMENT = "in_development"
        IN_QA = "in_qa"
        IN_CODE_REVIEW = "in_code_review"
        READY_FOR_RELEASE = "ready_for_release"
        RELEASED = "released"
        ARCHIVED = "archived"

    name = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=False)
    status = models.CharField(
        choices=Statuses.choices, max_length=255, default=Statuses.NEW_TASK
    )
    priority = models.PositiveSmallIntegerField(null=True, blank=False)
    author = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="authored_tasks",
        verbose_name="Author",
    )
    executor = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="executed_tasks",
        verbose_name="Executor",
    )
    tag = models.ManyToManyField(
        Tag, blank=True, related_name="tasks", verbose_name="Tag"
    )

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name

    def allowed_status_transitions(self):
        if self.status == "new_task":
            return ["in_development", "archived"]
        elif self.status == "in_development":
            return ["in_qa"]
        elif self.status == "in_qa":
            return ["in_development", "in_code_review"]
        elif self.status == "in_code_review":
            return ["ready_for_release", "in_development"]
        elif self.status == "ready_for_release":
            return ["released"]
        elif self.status == "released":
            return ["archived"]
        else:
            return []
