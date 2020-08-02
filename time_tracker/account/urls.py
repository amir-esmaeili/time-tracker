from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', sign_up, name='signup')
]