from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Bills(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    debt_amount = models.FloatField(max_length=6)
    text_comment = models.TextField(blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title


class Group(models.Model):
    group_name = models.CharField(max_length=20)

    def __str__(self):
        return self.group_name


class Debts(models.Model):
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    percent = models.FloatField()
    amount_paid = models.FloatField()


class GroupUsers(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
