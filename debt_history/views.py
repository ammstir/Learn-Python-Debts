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

            for user in group.users.exclude(id=current_user.id).all():
                debt = Debt(user=user, bill=bill)
                debt.save()

            return render(request, 'debt_history/make_debts.html', {'form': form})
    else:
        form = AddBill(request.user)
    return render(request, 'debt_history/make_debts.html', {'form': form})


def make_login(request):
    login = LoginForm(request.POST)
    return render(request, 'debt_history/make_login.html', {'form': login})


