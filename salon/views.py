from django.shortcuts import render
from .forms import ServiceForm 
from .models import Barber

# Create your views here.

def index(request):    
        form = ServiceForm()
        # context = { 'form': ServiceForm() }  
        return render(request, 'index.html', {'form': form})

def load_barbers(request):
    service_id = request.GET.get('service')
    barbers = Barber.objects.filter(services = service_id)
    return render(request, 'barber_options.html', {'barbers': barbers})