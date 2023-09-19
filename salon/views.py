from django.shortcuts import render
from .forms import ServiceForm 
from .models import Barber, WorkingHours

# Create your views here.

def index(request):    
        form = ServiceForm()
        return render(request, 'index.html', {'form': form})

def barbers(request):    
    service_id = request.GET.get("service")    
    barbers = Barber.objects.filter(services = service_id)   
    return render(request, 'barbers.html', {'barbers': barbers})

def working_days(request):
    barber = request.GET.get("barber") 
    working_days = WorkingHours.objects.filter(barber=barber)
    return render(request, 'working_days.html', {'working_days': working_days})