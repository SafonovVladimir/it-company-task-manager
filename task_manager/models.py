from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Worker(AbstractUser):
    position = models.ForeignKey(
        "Position",
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return (
            f"{self.username} "
            f"({self.first_name} {self.last_name}, "
            f"{self.position})"
        )

    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", kwargs={"pk": self.pk})


class Position(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


PRIORITY_CHOICES = (
    ("Urgent", "Urgent"),
    ("High", "High"),
    ("Medium", "Medium"),
    ("Low", "Low")
)


class Task(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey("TaskType", on_delete=models.DO_NOTHING)
    assignees = models.ManyToManyField(Worker, related_name="tasks")
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("task_manager:task-detail", kwargs={"pk": self.pk})


class TaskType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name
