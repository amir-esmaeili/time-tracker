from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, blank=False)
    tag = models.CharField(max_length=100)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField()
