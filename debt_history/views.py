
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import Sum
from debt_history.models import *
from .forms import RegisterForm, AddBill, AddGroup, ShowGroup
from .models import Bill, Group, Debt

# from django.views.generic.edit import FormView
# from django.contrib.auth.forms import UserCreationForm
# from django import forms


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


def logout_view(request):
    logout(request)
    return render(request, 'registration/my_logout.html')


@login_required
def add_group(request):
    if request.method == "POST":
        form = AddGroup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('debt_list')

    else:
        form = AddGroup()
    return render(request, 'debt_history/add_group.html', {'form': form})


@login_required
def make_bill(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddBill(current_user, request.POST)
        if form.is_valid():
            data = form.cleaned_data
            bill = Bill(author=current_user, title=data['title'],
                        debt_amount=data['debt_amount'], text_comment=data['text_comment'])
            bill.save()

            group = Group.objects.get(id=int(form.cleaned_data['group']))
            percent = round(100/len(group.users.all()), 2)

            for user in group.users.exclude(id=current_user.id).all():
                debt = Debt(user=user, bill=bill, percent=percent)
                debt.save()
            
            return redirect('debt_list')
            
    else:
        form = AddBill(request.user)
    return render(request, 'debt_history/make_debts.html', {'form': form})

@login_required
def debt_list(request):
    debt_l = Debt.objects.all()
    debts = []
    for debt in debt_l:
        id = debt.id
        bill = debt.bill.title
        amount = round(debt.bill.debt_amount * debt.percent / 100, 2)
        participant = debt.user.username
        debts.append({'id': id, 'billname': bill, 'amount': amount, 'participant': participant})

    debts_by_user = {}
    for debt in debts:
        if debt['participant'] in debts_by_user:
            debts_by_user[debt['participant']] += debt['amount']
        else:
            debts_by_user[debt['participant']] = debt['amount']
    print(debts_by_user)

    total_balance = {}
    total_balance = Bill.objects.aggregate(Sum('debt_amount'))
    

    

    return render(request, 'debt_history/debt_list.html', {'debt_list': debts, 'debts_by_user': debts_by_user, 'total_balance': total_balance})

#просто выводит все объекты модели Bill
def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'debt_history/bills_list.html', {'bill_list': bills})

@login_required
def group_list(request):
    current_user = request.user
    form = ShowGroup(current_user)
    return render(request, 'dash/dashleftbar.html', {'form': form})

    


def whom_how_much(request):
    user_id = request.user.id
    debts = Debt.objects.filter(user_id=user_id)
    whom = {}
    for debt in debts:
        name = debt.bill.author.username
        amount = round(debt.bill.debt_amount * debt.percent / 100, 2)
        if name not in whom:
            whom.update({name: amount})
        else:
            whom[name] += amount

    return render(request, 'debt_history/my_debts.html', {'whom': whom})





