from django.urls import path
from .views import ReportView


urlpatterns = [
    path('<slug:period>/', ReportView.as_view(), name='report')
]