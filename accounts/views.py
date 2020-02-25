from django.contrib.auth.models import Group
from .models import User

from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'templates/userinterfacedesign/index.html'


class CreateGroupview(CreateView):
    model = Group
    form_class = forms.GroupForm
    redirect_field_name ='templates/group_detail.html'


def index(request):
    



    return render(request,"userinterfacedesign/login.html",)



#######################    REST API        #################################

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#######################    REST API        #################################
