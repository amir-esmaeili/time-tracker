from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('time_tracker.api.urls')),
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.jwt')),
]
