from django.urls import path
from .views import make_debt, registration


urlpatterns = [
    path('debt/', make_debt, name='make_debt'),
    path('register/', registration, name='register'),

]