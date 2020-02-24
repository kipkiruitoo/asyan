from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.username