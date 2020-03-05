from django import template
from django.contrib.auth.models import Group
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
register = template.Library()


factory = APIRequestFactory()
request = factory.get('/')


serializer_context = {
    'request': Request(request),
}


@register.filter(name='has_group')
def has_group(user, group_name):
    user = User.objects.get(username=user)
    us = UserSerializer(user, context=serializer_context)
    # print(us.data)
    group = Group.objects.get(name=group_name)
    print(us)
    print(user.groups)
    return True if group_name in us.data.groups else False
