from django.urls import path
from .views import signup, profile


urlpatterns = [
    path('', signup, name='signup'),
    path('me/', profile, name='profile')
]