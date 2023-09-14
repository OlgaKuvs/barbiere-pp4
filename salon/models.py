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
    is_available = models.BooleanField(default=True, null=False, blank=False) 

    def __str__(self):
        return self.name
    

class Working_hours(models.Model):
    barber = models.ForeignKey(to=Barber, on_delete=models.CASCADE)
    time_start = models.DateTimeInput(auto_now=False, auto_now_add=False)
    time_end = models.DateTimeInput(auto_now=False, auto_now_add=False)


