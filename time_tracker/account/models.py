from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Accounts(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=3)

    REQUIRED_FIELDS = [email, name]

    def __str__(self):
        return self.email
