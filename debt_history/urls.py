from django.urls import path
from .views import registration, logout_view, make_bill, make_login, debt_list, bill_list


urlpatterns = [
    path('register/', registration, name='register'),
    #path('group/new', group_list, name='group'),
    path('logout/', logout_view, name='logout'),
    path('login/', make_login, name='make_login'),
    path('bills/new/', make_bill, name='make_bill'),
    path('debt/list/', debt_list, name='debt_list'),
    path('bills/list/', bill_list, name='bill_list'),
]
