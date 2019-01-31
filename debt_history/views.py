from django.shortcuts import render
from .forms import LoginForm, AddBill


def make_bill(request):
    form = AddBill(request.POST)
    new_bill = form.save()
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


