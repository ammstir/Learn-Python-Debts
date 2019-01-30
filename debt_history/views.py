from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from debt_history.models import *
from .forms import LoginForm, RegisterForm
from .models import Debts

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


        

def make_debt(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid:
            return render(request, 'debt_history/make_debt.html', {'form': form})

        debt = Debts(
            
        )
        bills = Bill
        return

    form = LoginForm()
    return render(request, 'debt_history/make_debt.html', {'form': form})