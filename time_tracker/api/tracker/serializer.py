from rest_framework import serializers
from .models import Task, Project


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['uuid', 'title', 'tag', 'project', 'start_time', 'end_time']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']
