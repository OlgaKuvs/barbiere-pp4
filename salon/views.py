from django.shortcuts import render, redirect, get_object_or_404
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
    """
    Renders the home page. Get all services and barbers
    from the database to show on home page.
    """
    services = Service.objects.all()
    barbers = Barber.objects.all()
    context = {'services': services, 'barbers': barbers}
    return render(request, 'index.html', context)


def booking(request):
    """
    Renders the booking page. Get all services from the database.
    Returns rendered booking page.
    """
    services = Service.objects.all()
    return render(request, 'booking.html', {'services': services})


@login_required
def save_form(request):
    """
    Saves booking data to the database.
    Redirects to user profile page.
    """
    if request.method == 'POST':
        customer = request.user
        service = request.POST.get('service')
        barber = request.POST.get('barber')
        barber_days = request.POST.get('working_days')
        format = "%A, %d %B, %Y   %H:%M"
        date = datetime.strptime(barber_days, format)

        booking = Booking.objects.create(
            customer=customer,
            barber=Barber.objects.get(id=int(barber)),
            date=date,
            service=Service.objects.get(id=int(service)),
            )
        messages.info(request, 'Your booking has been created.')
        booking.save()
    return redirect('user_profile')


def barbers(request):
    """
    Handles htmx requests to load barbers list to booking page.
    """
    service_id = request.GET.get("service")
    barbers = Barber.objects.filter(services=service_id, is_available=True)
    context = {'barbers': barbers, 'is_htmx': True}
    return render(request, 'barbers.html', context)


def working_days(request):
    """
    Handles htmx requests to load time slots
    for chosen service and barber to booking page.
    """
    barber = request.GET.get("barber")
    barber_days = WorkingHours.objects.filter(barber=barber)
    next_week = available_weekday(7)
    time_slots = get_time_slots(next_week, barber_days)
    visit_times = checkDay(barber, time_slots)
    context = {'visit_times': visit_times}
    return render(request, 'working_days.html', context)


def available_weekday(days):
    """
    Loop days you want in the next 7 days
    """
    free_dates = []
    for i in range(0, days):
        next_day = datetime.now() + timedelta(1)
        a = next_day + timedelta(days=i)
        free_dates.append(a)
    return free_dates


def checkDay(barber, all_times):
    """
    Gets available days and times for given barber
    """
    dates = []
    for day in all_times:
        day_time = datetime.strptime(day, "%A, %d %B, %Y  %H:%M")
        if Booking.objects.filter(barber=barber, date=day_time).count() < 1:
            day_time = day_time.strftime("%A, %d %B, %Y   %H:%M")
            dates.append(day_time)
    return dates


def get_time_slots(next_week, barber_days):
    # Gets list of time slots for next next_week days
    all_times = []
    for next_day in next_week:
        for work_day in barber_days:
            day_of_week = next_day.weekday()
            if work_day.day_of_week == day_of_week:
                start_time = work_day.time_start
                next_time = datetime.combine(next_day.date(), start_time)
                while next_time.hour < work_day.time_end.hour:
                    free_time = next_time.strftime("%A, %d %B, %Y   %H:%M")
                    all_times.append(free_time)
                    next_time = next_time + timedelta(hours=1)
    return(all_times)


def edit_booking(request, id):
    """
    GET: renders edit_booking page for given booking.
    POST: saves edited appointment for given user and
    returns profile page with updated bookings info.
    """
    if request.method == 'POST':
        customer = request.user
        service = request.POST.get('service')
        barber = request.POST.get('barber')
        barber_days = request.POST.get('working_days')
        format = "%A, %d %B, %Y   %H:%M"
        date = datetime.strptime(barber_days, format)
        booking = Booking.objects.filter(id=id).update(
            customer=customer,
            barber=Barber.objects.get(id=int(barber)),
            date=date,
            service=Service.objects.get(id=int(service)),
            )
        messages.success(
            request, str(customer) + ', your appointment is changed!'
            )
        return redirect('user_profile')
    else:
        booking = get_object_or_404(Booking, id=id)
        services = Service.objects.all()
        barbers = Barber.objects.filter(services=booking.service)
        visit_times = edit_working_days(booking.barber).get('visit_times')
        new_date = booking.date.strftime("%A, %d %B, %Y   %H:%M")
        context = {'services': services,
                   'barbers': barbers,
                   'booking': booking,
                   'new_date': new_date,
                   'visit_times': visit_times}
        return render(request, 'edit_booking.html', context)
    

def edit_working_days(barber):
    """
    Loads the working weekdays of chosen barber from db,
    generates timeslots and returns them.
    """
    barber_days = WorkingHours.objects.filter(barber=barber)
    next_week = available_weekday(7)
    time_slots = get_time_slots(next_week, barber_days)
    visit_times = checkDay(barber, time_slots)
    context = {'visit_times': visit_times}
    return (context)


def delete_booking(request, id):
    """
    Cancel given booking.
    """
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        booking.delete()
        messages.info(request, 'Your booking has been cancelled.')
        return redirect('user_profile')
    return render(request, 'delete_booking.html', {'booking': booking})


def user_registration(request):
    """
    Registers the user.
    GET: Renders registration page.
    POST: Registers user and redirects to user login page.
    """
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, user + ', your account is created successfully!'
                )
            return redirect('user_login')
        else:
            messages.error(request, "Please fill out all fields")
            context = {'form': form}
            return render(request, 'registration.html', context)

    form = CustomerForm()
    context = {'form': form}
    return render(request, 'registration.html', context)


def user_login(request):
    """
    Logs in the user.
    GET: Renders login page.
    POST: Logs in user and redirects to profile page.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(
                request, username + ', you are successfully logged in!'
                )
            login(request, user)
            bookings = Booking.objects.filter(customer=request.user)
            if bookings:
                return redirect('user_profile')
            else:
                return redirect('booking')
        else:
            messages.info(
                request, 'Username or password is wrong! Try again...'
                )
            return redirect('user_login')
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)


def user_profile(request):
    """
    Renders user profile page with a list of bookings and next day date.
    """
    bookings = Booking.objects.filter(customer=request.user).order_by('-date')
    next_day = datetime.now() + timedelta(hours=12)
    context = {'bookings': bookings,'next_day': next_day}
    return render(request, 'profile.html', context)


def user_logout(request):
    """
    Logs out the user and redirects to home page.
    """
    auth.logout(request)
    return redirect('index')
