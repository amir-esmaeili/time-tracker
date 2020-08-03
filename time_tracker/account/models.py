from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.email
