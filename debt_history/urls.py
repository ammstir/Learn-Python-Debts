from django.urls import path
from .views import registration, logout_view, make_bill, debt_list, bill_list, add_group


urlpatterns = [
    path('register/', registration, name='register'),
    path('group/new/', add_group, name='newgroup'),
    path('logout/', logout_view, name='logout'),
    path('bills/new/', make_bill, name='make_bill'),
    path('debt/list/', debt_list, name='debt_list'),
    path('bills/list/', bill_list, name='bill_list'),
    path('debts/my/', whom_how_much, name='whom_how_much'),
]
