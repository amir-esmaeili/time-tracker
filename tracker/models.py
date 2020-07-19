from uuid import uuid4

from django.db import models


class Project(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)


class Task(models.Model):
    tag_choices = [
        ('p', 'Personal'),
        ('c', 'Client'),
    ]

    title = models.CharField(max_length=200, blank=False)
    uuid = models.UUIDField(default=uuid4)
    tag = models.CharField(max_length=50, choices=tag_choices)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(null=True)
