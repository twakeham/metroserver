from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=True)
    sunday = models.BooleanField(default=True)


class Suburb(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    zone = models.ForeignKey(Zone)

