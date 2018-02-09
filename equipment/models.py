from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(u'车名', max_length=10)


class Driver(models.Model):
    name = models.CharField(u'人名',max_length=10)
    car = models.ForeignKey(Car, related_name='drivers', on_delete=models.CASCADE, verbose_name='司机')
