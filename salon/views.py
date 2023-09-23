from django.shortcuts import render
from django.contrib import messages
from datetime import datetime, timedelta
import time
from .forms import ServiceForm 
from .models import Barber, WorkingHours, Service

# Create your views here.

def index(request):    
        form = ServiceForm()
        # services = Service.objects.all()
        return render(request, 'index.html', {'form': form})

def barbers(request):    
    service_id = request.GET.get("service")    
    barbers = Barber.objects.filter(services = service_id)   
    return render(request, 'barbers.html', {'barbers': barbers})

def working_days(request):
    barber = request.GET.get("barber")    
    working_days = WorkingHours.objects.filter(barber=barber)    
    next_week = available_weekday(8)  
   
    visit_times = []
    for next_day in next_week:
        for work_day in working_days:       
            day_of_week = next_day.weekday()            
            if work_day.day_of_week == day_of_week:                
                start_time = work_day.time_start                
                next_time = datetime.combine(next_day.date(), start_time)
             
                while next_time.hour < work_day.time_end.hour:
                    visit_time = next_time.strftime("%A, %d %B, %Y   %H:%M")                    
                    visit_times.append(visit_time)
                    next_time = next_time + timedelta(hours=1) 
                    
                    
                print("sss", visit_times)               
             
       
    return render(request, 'working_days.html', 
            {'visit_times': visit_times},                       
           )


def available_weekday(days):
    #Loop days you want in the next 7 days:   
    free_dates = []
    for i in range (0, days):
        next_day = datetime.now() + timedelta(1)
        a = next_day + timedelta(days=i) 
        free_dates.append(a)           
    return free_dates


