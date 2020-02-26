from django.db import models

# Create your models here.
from accounts.models import User


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_admin')
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    registered_on = models.DateField(auto_now_add=True)

