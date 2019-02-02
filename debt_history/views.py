from django.shortcuts import render
from .forms import LoginForm, AddBill
from .models import Bill


def make_bill(request):
    if request.method == 'POST':
        form = AddBill(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            bill = Bill(author=request.user, title=data['title'],
                        debt_amount=data['debt_amount'], text_comment=data['text_comment'])
            bill.save()
            return render(request, 'debt_history/make_debts.html', {'form': form})
    else:
        form = AddBill()
        return render(request, 'debt_history/make_debts.html', {'form': form})


def make_login(request):
    login = LoginForm(request.POST)
    return render(request, 'debt_history/make_login.html', {'form': login})

# Create your views here.
# def make_debt(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if not form.is_valid:
#             return render(request, 'debt_history/make_debt.html', {'form': form})
#
#         # debt = Debts(
#         #
#         #  )
#         # bills = Bill
#         # return
#
#      form = LoginForm()
#     return render(request, 'debt_history/make_debt.html', {'form': form})


