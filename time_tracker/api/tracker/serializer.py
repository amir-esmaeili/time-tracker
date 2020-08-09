from rest_framework import serializers
from .models import Task, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class TasksSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = Task
        fields = '__all__'


class NewTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


