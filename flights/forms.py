from django import forms
from .models import Airport, Flight

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'city']

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'duration']
