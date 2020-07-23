from django.urls import path
from .views import TasksView, TaskView, ProjectView


urlpatterns = [
    path('', TasksView.as_view(), name='all-tasks'),
    path('task/', TaskView.as_view(), name='a-task'),
    path('task/<slug:uuid>/', TaskView.as_view(), name='delete'),
    path('project/', ProjectView.as_view(), name='project')
]
