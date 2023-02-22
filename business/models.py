from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


class Seller(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    credit = models.BigIntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return f'name = {self.name}'


class ChargeRecord(models.Model):
    seller = models.ForeignKey(to=Seller, on_delete=models.CASCADE)
    customer = PhoneNumberField(max_length=150, null=True, blank=True)
    amount = models.PositiveIntegerField(null=False, blank=False, editable=False)
    created_date = models.DateTimeField(default=datetime.now, blank=False, null=False)

    def __str__(self):
        return f'seller = {self.seller}, customer = {str(self.customer)}, amount = {self.amount},' \
               f' date = {self.created_date}'

