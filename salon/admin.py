from django.contrib import admin
from .models import *


admin.site.register(Service)
admin.site.register(Barber)
admin.site.register(WorkingHours)
admin.site.register(Booking)

