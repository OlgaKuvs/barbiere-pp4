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
    # print("aaa", barber)
    working_days = WorkingHours.objects.filter(barber=barber)
    next_week = available_weekday(8)     
    string_days = []
    for next_day in next_week:
        for work_day in working_days:       
            day_of_week = next_day.weekday()            
            if work_day.day_of_week == day_of_week:
                string_day = next_day.strftime("%A, %d %B, %Y")
                string_days.append(string_day)
                # print(string_days)            
       
    return render(request, 'working_days.html', 
            {'string_days': string_days}, 
            # {'working_days': working_days},            
           )


def available_weekday(days):
    #Loop days you want in the next 7 days:   
    free_dates = []
    for i in range (0, days):
        next_day = datetime.now() + timedelta(1)
        a = next_day + timedelta(days=i) 
        free_dates.append(a)           
    return free_dates


def working_hours(request):
    working_day = request.GET.get("working_days")
           
    dw = working_day.split(',')[0]
    print(dw)
    weekday_as_int = time.strptime(dw,"%A").tm_wday   
    
    working_hours = WorkingHours.objects.filter(day_of_week=weekday_as_int)
    
    #wh = working_hours.values_list('time_start')
    #print("sss", wh) 
    print("zzz", working_hours)       
        
    
    return render(request, 'working_hours.html', {'working_hours': working_hours})
