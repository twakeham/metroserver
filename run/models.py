from django.db import models

import driver.models


class Run(models.Model):
    name = models.CharField(max_length=100)
    delivery_date = models.DateField()
    driver = models.ForeignKey(driver.models.Driver)

    complete = models.BooleanField(default=False)
    manifested = models.BooleanField(default=False)
    invoiced = models.BooleanField(default=False)
    canceled = models.NullBooleanField(default=False)

    def __str__(self):
        return self.name
