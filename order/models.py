from django.db import models

import suburb.models
import run.models
import user.models
import product.models


class OrderProduct(models.Model):
    order = models.ForeignKey('Order')
    product = models.ForeignKey(product.models.Product)
    quantity = models.IntegerField()


class Order(models.Model):
    reference = models.CharField(max_length=64)
    name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, null=True)
    suburb = models.ForeignKey(suburb.models.Suburb)
    phone1 = models.CharField(max_length=24)
    phone2 = models.CharField(max_length=24, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    preferred_day = models.CharField(max_length=20, default='', null=True)
    delivery_date = models.DateField(null=True)
    delivery_timeframe = models.CharField(max_length=30, null=True)

    products = models.ManyToManyField(product.models.Product, through=OrderProduct)
    meterage = models.FloatField(null=True)
    price = models.FloatField()

    run = models.ForeignKey(run.models.Run, null=True)
    sequence = models.IntegerField(null=True)

    confirmed = models.NullBooleanField(default=False, null=True)
    canceled = models.NullBooleanField(default=False, null=True)
    completed = models.NullBooleanField(default=False, null=True)
    flag = models.NullBooleanField(default=False, null=True)

    user = models.ForeignKey(user.models.User)


class History(models.Model):
    order = models.ForeignKey(Order)
    description = models.TextField()
    user = models.ForeignKey(user.models.User)


class Note(models.Model):
    order = models.ForeignKey(Order)
    text = models.TextField()
    user = models.ForeignKey(user.models.User)


class Flags(models.Model):
    order = models.ForeignKey(Order)
    text = models.TextField()
    user = models.ForeignKey(user.models.User)

