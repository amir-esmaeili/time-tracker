from django.urls import path
from .views import TasksView, ProjectsView, TasksModifyView


urlpatterns = [
    path('', TasksView.as_view(), name='all_tasks'),
    path('<slug:uuid>/', TasksModifyView.as_view(), name='a_task'),
]
