from django import template
from django.contrib.auth.models import Group
from accounts.serializers import UserSerializer
from  accounts.models import User
register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    user = User.objects.filter(username=user)
    us = UserSerializer(user)
    print(us.data)
    # group = Group.objects.filter(name=group_name)
    # print(user)
    # return True if group in user.groups else False
