from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AirportForm, FlightForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        if 'add_airport' in request.POST:
            airport_form = AirportForm(request.POST)
            if airport_form.is_valid():
                airport_form.save()
                return redirect('/')
        elif 'add_flight' in request.POST:
            flight_form = FlightForm(request.POST)
            if flight_form.is_valid():
                flight_form.save()
                return redirect('/')
    else:
        airport_form = AirportForm()
        flight_form = FlightForm()

    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(), 'airport_form': airport_form, 'flight_form': flight_form})


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
