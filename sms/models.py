from django.db import models

import user.models


class Message(models.Model):
    phone = models.CharField(max_length=24)
    text = models.TextField()

    sent = models.BooleanField()
    user = models.ForeignKey(user.models.User)