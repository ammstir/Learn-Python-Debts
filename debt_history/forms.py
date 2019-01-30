from django import forms
from debt_history.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
