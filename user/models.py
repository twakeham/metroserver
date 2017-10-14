from django.db import models


class Permissions(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    description = models.CharField(max_length=200)


class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    super_user = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    permissions = models.ManyToManyField(Permissions)


