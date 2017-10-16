from django.db import models

import user.models
import order.models


class Message(models.Model):
    phone = models.CharField(max_length=24)
    text = models.TextField()
    sent = models.BooleanField()

    order = models.ForeignKey(order.models.Order, null=True)
    user = models.ForeignKey(user.models.User)
    timestamp = models.DateTimeField()