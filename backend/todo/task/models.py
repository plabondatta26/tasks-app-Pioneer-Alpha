from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class DirectoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text="Directory creator")
    title = models.CharField(max_length=100, blank=True, null=True, help_text="Title of the directory")

    class Meta:
        db_table = 'directories'

    def __str__(self):
        return self.title


class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text="Task creator")
    title = models.CharField(max_length=100, blank=True, null=True, help_text="Title of the task")
    description = models.TextField(max_length=1000, blank=True, null=True, help_text="Description of the task")
    date = models.DateField(blank=True, null=True, help_text="Targeted date for complete the task")
    directory = models.ForeignKey(DirectoryModel, on_delete=models.CASCADE,
                                  blank=True, null=True, help_text="Task directory")
    is_important = models.BooleanField(default=False, help_text="Is the task is important or not")
    is_completed = models.BooleanField(default=False, help_text="Is the task is completed or not")

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return self.title
