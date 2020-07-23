from datetime import datetime
from .serializer import TasksSerializer, ProjectSerializer
from .models import Task, Project
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TasksView(APIView):

    def get(self, request):
        """
        Returns all of tasks
        """
        done = Task.objects.filter(end_time__isnull=False)
        tasks = Task.objects.filter(end_time__isnull=True)
        serializer_done = TasksSerializer(done, many=True)
        serializer_tasks = TasksSerializer(tasks, many=True)
        return Response({'tasks': serializer_tasks.data,
                         'done': serializer_done.data,
                         'len': len(serializer_tasks.data)+len(serializer_done.data)})

    def post(self, request):
        """
        Adds a new task to database
        """
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'message': 'New task added', 'task': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Deletes all of the tasks
        """
        Task.objects.all().delete()
        return Response({'message': 'All tasks deleted'}, status=status.HTTP_200_OK)


class TaskView(APIView):

    def get_object(self, task_uuid):
        """
        Finds and returns an object based on the key provided
        """
        try:
            return Task.objects.get(uuid=task_uuid)
        except Task.DoesNotExist:
            return Http404

    def put(self, request):
        """
        Updates the task => mainly for finishing task
        """
        try:
            task = self.get_object(request.data['uuid'])
        except Task.DoesNotExist:
            return Http404
        serializer = TasksSerializer(task, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'updated', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        """
        Delete task based on the uuid
        """
        try:
            task = Task.objects.get(uuid=uuid)
            task.delete()
            return Response({'message': 'task deleted'})
        except Task.DoesNotExist:
            return Http404
        except KeyError:
            return Response({'message': 'body doesn\'t contain uuid'})


class ProjectView(APIView):

    def get(self, request):
        """
        Sends all of the projects
        """
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response({'projects': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Add new project
        """
        serializer = ProjectSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'New project added', 'project': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Delete project based on the uuid
        """
        try:
            uuid = request.data['uuid']
            project = Project.objects.get(uuid=uuid)
            project.delete()
            return Response({'message': 'project deleted'})
        except Project.DoesNotExist:
            return Http404
        except KeyError:
            return Response({'message': 'body doesn\'t contain uuid'})
