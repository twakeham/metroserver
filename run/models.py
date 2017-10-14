from django.db import models

import driver.models


class Run(models.Model):
    name = models.CharField(max_length=100)
    delivery_date = models.DateField()
    driver = models.ForeignKey(driver.models.Driver)

    complete = models.BooleanField(default=False)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
