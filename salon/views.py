from django.shortcuts import render
from salon.forms import ServiceForm

# Create your views here.

def index(request):
    context = { 'form': ServiceForm() }
    return render(request, 'index.html', context)