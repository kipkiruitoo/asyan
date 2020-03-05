from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm ,UserChangeForm
from django.contrib.auth.models import Group
from django import forms
from .models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}),
                               required=True)
    class Meta:
        model = User
        fields = ['username', 'password']


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


class UserChangeForm(UserChangeForm):
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone= forms.CharField(max_length=15, widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','phone']
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text='<div class="form-text text-muted"><small>Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.</small></div>'
        self.fields['password'].help_text= " <a href=\"../changepassword/\" class='btn btn-custon-two'>Click Here</a to reset your Password."


class PasswordChangeForm(PasswordChangeForm):
    
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'