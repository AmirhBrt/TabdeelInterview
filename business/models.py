from django.db import models
from datetime import datetime


class Seller(models.Model):
    name = models.CharField(max_length=150, blank=False, unique=True)
    credit = models.BigIntegerField(blank=True, default=0)

    def __str__(self):
        return f'name= {self.name}, credit= {self.credit}'


class Customer(models.Model):
    name = models.CharField(max_length=150, blank=True)
    charge = models.BigIntegerField(blank=True, default=0)

    def __str__(self):
        return f'name= {self.name}, charge={self.charge}'


class ChargeRecord(models.Model):
    seller = models.ForeignKey(to=Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'seller = {self.seller.name}, customer = {self.customer.name}, date = {self.created_date}'

