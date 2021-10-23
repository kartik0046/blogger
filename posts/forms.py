from .models import *
from django.forms import ModelForm
class AskQuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=['body']

class AddAnswer(ModelForm):
    class Meta:
        model=Answer
        fields=['body']
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import *
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class AccountSettings(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user','email']
