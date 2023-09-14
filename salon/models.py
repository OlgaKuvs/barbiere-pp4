from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    

class Barber(models.Model):
    name = models.CharField(max_length=50, unique=True)
    services = models.ManyToManyField(Service, related_name ='services')
    is_available = models.BooleanField(
        default=True, 
        null=False, 
        blank=False) 

    def __str__(self):
        return self.name
    

class WorkingHours(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='barber')
    date = models.DateField(
        auto_now=False, 
        auto_now_add=False, 
        null=False, 
        blank=False, 
        verbose_name="Date")
    time_start = models.TimeField(
        auto_now=False, 
        auto_now_add=False,
        null=False, 
        blank=False, 
        verbose_name="Start time")
    time_end = models.TimeField(
        auto_now=False, 
        auto_now_add=False,
        null=False, 
        blank=False, 
        verbose_name="End time")

    class Meta:
        verbose_name = 'Working Hours'
        verbose_name_plural = 'Working Hours' 

    def __str__(self):
        return f"{self.barber}, {self.date} {self.time_start} - {self.time_end}"
    



    





