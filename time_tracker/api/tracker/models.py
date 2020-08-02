from uuid import uuid4

from django.db import models
from time_tracker.account.models import Accounts


class Project(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Accounts, null=True, on_delete=models.CASCADE)


class Task(models.Model):
    tag_choices = [
        ('personal', 'Personal'),
        ('client', 'Client'),
    ]

    title = models.CharField(max_length=200, blank=False)
    uuid = models.UUIDField(default=uuid4)
    tag = models.CharField(max_length=50, choices=tag_choices)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    user = models.ForeignKey(Accounts, null=True, on_delete=models.CASCADE)
