from django.db import models


class Driver(models.Model):
    driver_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    meterage = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{0} {1}'.format(self.driver_number, self.name)



