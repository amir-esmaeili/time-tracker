from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('time_tracker.api.urls')),
    path('users/', include('time_tracker.account.urls')),
    path('auth/login/', jwt_views.TokenObtainPairView.as_view(), name='login')
]
