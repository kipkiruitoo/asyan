from django.db import models
from inventory.models import Warehouse
from django.contrib.auth.models import Group
# Create your models here.

class department(models.Model):
    departments_name= models.CharField(max_length=40, unique=True)
    warehouse_name= models.OneToOneField(Warehouse,on_delete=models.CASCADE,primary_key=True,)
    departments_user_group= models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    description = models.TextField(default=False)
    
    def __str__(self):
        return self.departments_name