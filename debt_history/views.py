from django.shortcuts import render
from .forms import LoginForm, AddBill


def make_bill(request):
    form = AddBill(request.POST)
    return render(request, 'debt_history/make_debts.html', {'form': form})


def make_login(request):
    login = LoginForm(request.POST)
    return render(request, 'debt_history/make_login.html', {'form': login})



