from django.urls import include, path
from time_tracker.api.tracker.views import ProjectModifyView, ProjectsView

urlpatterns = [
    path('tasks/', include('time_tracker.api.tracker.urls')),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<slug:uuid>/', ProjectModifyView.as_view(), name='project'),
    path('reports/', include('time_tracker.api.report.urls'))
]