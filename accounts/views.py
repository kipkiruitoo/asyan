from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import LoginForm ,PasswordChangeForm ,UserChangeForm
from .models import User

from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


# Create your views here.

def user_login(request):
    template = 'auth/login.html'
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if not User.objects.filter(email=username).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Account name '+username + ' doest not exists.'
                })
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Wrong password for account name '+ username
                })
        else:
            return render(request, template, {'form': form})
    else:
        form = LoginForm()

    return render(request, template, {'form': form})


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'auth/register.html'


class CreateGroupview(CreateView):
    model = Group
    form_class = forms.GroupForm
    redirect_field_name ='templates/group_detail.html'




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
#  change password logged in user function
# def change_password(request):
#     if request.method =='POST':
#             form = PasswordChangeForm(request.POST,User=request.User)
            
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Profile details updated.')
#                 return redirect('login')
                
#             else:
#                 messages.error(request, 'Profile Update denied.')
#                 return render(request, 'signup')
#     return render(request, 'auth/changepass.html')
        


# function for testing templates do not delete 
def index(request):
    return render(request, 'userinterfacedesign/mail.html')
def editprofile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ("Your Profile Updated"))
            return redirect('home')
    else:
        form = UserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'auth/editprofile.html', context)


# user password change form

def changepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Your Password Changed", extra_tags='green')
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'auth/changepassword.html', context)

