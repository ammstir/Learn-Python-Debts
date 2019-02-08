from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Bill(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    debt_amount = models.FloatField(max_length=6)
    text_comment = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Group(models.Model):
    group_name = models.CharField(max_length=20)
    users = models.ManyToManyField(User, related_name='debt_groups')

    def __str__(self):
        return self.group_name


class Debt(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    percent = models.FloatField(default=100)
    amount_paid = models.FloatField(default=0.0)
    paid = models.BooleanField(default=False)

