from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ('__all__')



#User form
class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']