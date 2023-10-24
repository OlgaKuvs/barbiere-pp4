from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

DAYS = ((0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'),
        (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'),)


class Service(models.Model):
    # Service model for storing services data.
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default='')
    image = CloudinaryField("image", default='')

    def __str__(self):
        return self.name


class Barber(models.Model):
    # Barber model for storing barber data.
    name = models.CharField(max_length=50, unique=True)
    services = models.ManyToManyField(Service, related_name='services')
    description = models.TextField(default='')
    image = CloudinaryField("image", default='')
    is_available = models.BooleanField(
        default=True,
        null=False,
        blank=False)

    def __str__(self):
        return self.name


class WorkingHours(models.Model):
    # WorkingHours model for storing barber's working weekdays and hours
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE,
                               related_name='barbers')
    day_of_week = models.IntegerField(choices=DAYS, default=0)
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
        return f"""{self.barber}, day {self.day_of_week}, 
                time {self.time_start}-{self.time_end}"""


class Booking(models.Model):
    # Booking model for storing booking data.
    customer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='customers')
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE,
                               related_name='barber_list')
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                related_name='service_list')

    def __str__(self):
        return f"""User: {self.customer}, Barber: {self.barber}, 
                Service: {self.service}, Date: {self.date}"""
