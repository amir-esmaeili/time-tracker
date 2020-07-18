from .serializer import TasksSerializer
from .models import Task

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TasksView(APIView):

    """
    This class is for all tasks
    """

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response({'tasks': serializer.data, 'len': len(serializer.data)})

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'message': 'New task added', 'task': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
