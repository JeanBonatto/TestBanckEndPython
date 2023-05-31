from django.db import models
# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17)

    def __str__(self):
        return self.name

class DataEntry(models.Model):
    value = models.FloatField()
    date_time = models.DateTimeField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value)