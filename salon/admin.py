from django.contrib import admin
from .models import *


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    search_fields = ['name', 'price']


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_available', 'service']
    search_fields = ['name', 'services__name']

    def service(self, obj):
        if obj.services.all(): 
            return list(obj.services.all().values_list('name', flat=True))
        else:
            return 'NA'
        

@admin.register(WorkingHours)
class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ['barber', 'day_of_week', 'time_start', 'time_end']    
    search_fields = ['barber__name', 'day_of_week']
    list_filter = ['day_of_week', ]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'barber', 'service', 'date']
    search_fields = ['customer__username', 'barber__name', 'service__name', 'date']
    list_filter = ['service__name', 'barber__name', 'date']

