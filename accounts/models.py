from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    
class profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone= models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.user} Profile'
    