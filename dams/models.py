# dams/models.py
from django.db import models

class Dam(models.Model):
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.db import models

class DamStatistics(models.Model):
    # This will automatically use an AutoField named 'id'
    date = models.DateField()
    rainfall = models.FloatField()
    inflow = models.FloatField()
    power_house_discharge = models.FloatField()
    spillway_release = models.FloatField()
    dam = models.ForeignKey('Dam', on_delete=models.CASCADE)
