from django.shortcuts import render
from .forms import LoginForm, AddBill
from .models import Bill, Group, Debt


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

            return render(request, 'debt_history/make_debts.html', {'form': form})
    else:
        form = AddBill(request.user)
    return render(request, 'debt_history/make_debts.html', {'form': form})


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

    return render(request, 'debt_history/debt_list.html', {'debt_list': debts, 'debts_by_user': debts_by_user})


def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'debt_history/bills_list.html', {'bill_list': bills})


def make_login(request):
    login = LoginForm(request.POST)
    return render(request, 'debt_history/make_login.html', {'form': login})


