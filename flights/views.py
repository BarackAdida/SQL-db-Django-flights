from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request):
    return render(request, "flights/flights.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })