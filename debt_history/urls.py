from django.urls import path
from .views import make_bill, make_login

urlpatterns = [
    path('bills/new/', make_bill, name='make_bill'),
    path('login/', make_login, name='make_login'),
]
