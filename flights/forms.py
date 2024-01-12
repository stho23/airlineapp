from django import forms
from .models import Airport, Flight
from django.core.exceptions import ValidationError

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'city']

    def clean_code(self):
        code = self.cleaned_data['code']
        if Airport.objects.filter(code=code).exists():
            raise ValidationError("Airport with this code already exists.")
        return code

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'duration']

    def clean(self):
        cleaned_data = super().clean()
        origin = cleaned_data.get('origin')
        destination = cleaned_data.get('destination')

        if origin == destination:
            raise ValidationError("Origin and destination cannot be the same.")

        return cleaned_data
