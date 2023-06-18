from django.contrib import admin
from .models import DirectoryModel, TaskModel
# Register your models here.

admin.site.register(DirectoryModel)
admin.site.register(TaskModel)