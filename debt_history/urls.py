from django.urls import path
from .views import make_bill, make_login, debt_list, bill_list

urlpatterns = [
    path('bills/new/', make_bill, name='make_bill'),
    path('login/', make_login, name='make_login'),
    path('debt/list/', debt_list, name='debt_list'),
    path('bills/list/', bill_list, name='bill_list'),
]
