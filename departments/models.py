from django.db import models

# Create your models here.

class departments(models.Model):
    departments_name= models.CharField(max_length=40, unique=True)
    