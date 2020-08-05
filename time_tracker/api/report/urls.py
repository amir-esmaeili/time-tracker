from django.urls import path
from .views import ReportView


urlpatterns = [
    path('<slug:start>,<slug:end>/', ReportView.as_view(), name='report')
]