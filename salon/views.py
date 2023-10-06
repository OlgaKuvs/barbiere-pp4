from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .forms import CustomerForm, LoginForm 
from .models import Service, Barber, WorkingHours, Booking, User

# Create your views here.

def index(request):    
   return render(request, 'index.html')


def booking(request): 
    services = Service.objects.all()
    return render(request, 'booking.html', {'services': services }) 
          

@login_required     
def save_form(request):    
    if request.method == 'POST':
        customer = request.user
        service = request.POST.get('service')
        barber = request.POST.get('barber')       
        working_days = request.POST.get('working_days')      
        format = "%A, %d %B, %Y   %H:%M"
        date = datetime.strptime(working_days, format)
        
        booking = Booking.objects.create(
            customer=customer, 
            barber=Barber.objects.get(id=int(barber)),
            date=date, 
            service=Service.objects.get(id=int(service)),
            ) 
        booking.save()
    return redirect('user_profile')


def barbers(request):    
    service_id = request.GET.get("service")      
    barbers = Barber.objects.filter(services = service_id)   
    context = {'barbers': barbers, 'is_htmx': True}      
    return render(request, 'barbers.html', context )


def working_days(request):
    barber = request.GET.get("barber")    
    working_days = WorkingHours.objects.filter(barber=barber)    
    next_week = available_weekday(8)  
   
    all_times = []
    for next_day in next_week:
        for work_day in working_days:       
            day_of_week = next_day.weekday()            
            if work_day.day_of_week == day_of_week:                
                start_time = work_day.time_start                
                next_time = datetime.combine(next_day.date(), start_time)             
                while next_time.hour < work_day.time_end.hour:
                    free_time = next_time.strftime("%A, %d %B, %Y   %H:%M")                    
                    all_times.append(free_time)
                    next_time = next_time + timedelta(hours=1)
 
    visit_times = checkDay(barber, all_times)                        
    return render(request, 'working_days.html', {'visit_times': visit_times})


def available_weekday(days):
    # Loop days you want in the next 7 days   
    free_dates = []
    for i in range (0, days):
        next_day = datetime.now() + timedelta(1)
        a = next_day + timedelta(days=i) 
        free_dates.append(a)           
    return free_dates


def checkDay(barber, all_times):
    # Show only available days and times for exact barber 
    dates = []
    for day in all_times:        
        day_time = datetime.strptime(day, "%A, %d %B, %Y  %H:%M")
        if Booking.objects.filter(barber=barber, date=day_time).count() < 1:
            day_time = day_time.strftime("%A, %d %B, %Y   %H:%M")
            dates.append(day_time)
    return dates


def user_registration(request):    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ', your account is created successfully!')            
            return redirect('user_login')
        else: 
            messages.error(request, "Please fill out all fields")  
            context = {'form': form}
            return render(request, 'registration.html', context)            
    
    form = CustomerForm()
    context = {'form': form}
    return render(request, 'registration.html', context)


def user_login(request):    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, username + ', you are successfully logged in!')  
            login(request, user)                      
            return redirect('user_profile')
        else:
            messages.info(request, 'Username or password is wrong! Try again...')
            return redirect('user_login')
    else:
        form = LoginForm()       
        context = {'form': form}       
        return render(request, 'login.html', context)
    

def user_profile(request):
    bookings = Booking.objects.filter(customer=request.user)   
    context = {'bookings': bookings} 
    return render(request, 'profile.html', context)


def user_logout(request):    
    auth.logout(request)  
    return redirect('index')


















    
#Get stored data from django session:
    # customer = "Alex"    
    # service = request.session.get('service')
    # barber = request.session.get('barber')
    # working_days = request.session.get('working_days')
    # print("vvv", service)
    # booking_completed = Booking.objects.get_or_create(
    #             customer = customer,
    #             service = service,
    #             barber = barber,
    #             working_days = working_days,
    #         )
    # messages.success(request, "Booking saved!")
    # return redirect('booking')
       