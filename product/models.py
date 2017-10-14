from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    description = models.CharField(max_length=250)
    meterage = models.FloatField()

