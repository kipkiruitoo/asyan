from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django import forms
from .models import User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Display Name'
        self.fields['email'].label='Email Address'



class GroupForm(forms.ModelForm):
    class Meta():
        model = Group
        fields = '__all__'



