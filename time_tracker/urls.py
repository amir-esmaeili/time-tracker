from django.contrib import admin
from django.urls import path, include
from tracker.views import ProjectsView, ProjectModifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tasks/', include('tracker.urls')),
    path('api/v1/projects/', ProjectsView.as_view(), name='projects'),
    path('api/v1/projects/<slug:uuid>/', ProjectModifyView.as_view(), name='projects'),
    path('api/v1/report/', include('report.urls'))
]
