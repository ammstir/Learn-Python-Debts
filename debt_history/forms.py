from django import forms
from debt_history.models import *


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    email = forms.EmailField(label='Your email', max_length=40)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirmation_password = forms.CharField(label='Confirmation Password', widget=forms.PasswordInput)


class AddBill(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        group_choices = tuple((group.id, group.group_name) for group in user.debt_groups.all())
        self.fields['group'] = forms.ChoiceField(widget=forms.Select, choices=group_choices)

    class Meta:
        model = Bill
        exclude = ('author', 'created_date')


class AddGroup(forms.Form):
    group_name = forms.CharField(label='Group Name', max_length=20)
    participants = forms.MultipleChoiceField(label='Friends List')


class ShowAll(forms.Form):
    balance = forms.FloatField(label='Balance')
    you_owe = forms.FloatField(label='You Owe')
    you_are_owed = forms.FloatField(label='You are owed')
    friends_list = forms.CharField()


class AddFriend(forms.Form):
    friend_name = forms.CharField(label="Friend's name", max_length=20)
    friend_email = forms.EmailField(label="Friend's email", max_length=40)


class PayBill(forms.Form):
    friend = forms.CharField(label="Friend's name", max_length=20)
    amount = forms.FloatField(label='How much')
    date = forms.DateField(label='When was payed')


