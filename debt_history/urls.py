from django.urls import path
from .views import registration, logout_view, make_bill, common, bill_list, add_group, whom_how_much, money_return, group_list



urlpatterns = [
    path('register/', registration, name='register'),
    path('group/new/', add_group, name='newgroup'),
    path('logout/', logout_view, name='logout'),
    path('bills/new/', make_bill, name='make_bill'),
    path('', common, name='common'),
    path('bills/list/', bill_list, name='bill_list'),
    path('debts/my/', whom_how_much, name='whom_how_much'),
    path('return/', money_return, name='money_return'),
    path('group/list/', group_list, name='group_list'),
    #path('', main )


]
