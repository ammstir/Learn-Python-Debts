from django.urls import path
from .views import make_debt, registration, logout_view


urlpatterns = [
    path('debt/', make_debt, name='make_debt'),
    path('register/', registration, name='register'),
    #path('group/new', group_list, name='group'),
    path('logout/', logout_view, name='logout'),

]