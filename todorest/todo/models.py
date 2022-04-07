"""Models to manage the Users TODO list."""

# Std Import
from datetime import datetime
from pathlib import PurePath

# Site-package Import
from django.contrib.auth.models import User
from django.db import models

# Project Import


def image_directory_path(instance, filename):
    """Calculate an unique path for the uploaded image."""
  
    now = datetime.now()
    
    return PurePath(f'user_{instance.user.id}',
                    now.strftime("%Y"),
                    now.strftime("%m"),
                    now.strftime("%d"),
                    filename).as_posix()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "tasks")
    name = models.CharField(max_length = 100)
    image = models.FileField(upload_to = image_directory_path)
    deadline = models.DateTimeField(null = True)
    description = models.CharField(max_length = 300)
    creation_date = models.DateTimeField(auto_now_add = True)
    