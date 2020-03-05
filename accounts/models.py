from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django import template

# Create your models here.
register = template.Library()


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    head = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} Profile'


@register.filter(name='has_group')
def has_group(user, group_name):
    # group = Group.objects.get(name=group_name)
    # return True if group in user.groups.all() else False
    return user.groups.filter(name=group_name).exists()
