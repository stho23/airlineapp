from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import PassengerForm
from flights.models import Passenger

# Create your views here.
def index(request):
    passengers = Passenger.objects.all()
    passenger_list = []
    for passenger in passengers:
        first_name = passenger.first
        passenger_list.append(first_name)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html", {'passenger_list': passenger_list})

def passengers(request):
    passenger_form = PassengerForm()
    if request.method == 'POST':
        passenger_form = PassengerForm(request.POST)

        if passenger_form.is_valid():
            passenger = passenger_form.save(commit=False)
            passenger.first = passenger.first.lower()
            passenger.last = passenger.last.lower()
            passenger.save()
            return redirect("/")
    return render(request, 'users/passengers.html', {'passenger_form': passenger_form})

def registerUser(request):
    user_form = UserCreationForm()
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect("/users/")
    return render(request, 'users/signup.html', {'user_form': user_form})


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/users/")
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "users/login.html")

def logoutUser(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })