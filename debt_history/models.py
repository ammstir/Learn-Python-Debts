from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.group_name


class Debts(models.Model):
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    percent = models.FloatField()
    amount_paid = models.FloatField()
