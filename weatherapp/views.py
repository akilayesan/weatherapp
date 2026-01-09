from django.shortcuts import render
import requests
from .forms import cityForm
from django.conf import settings
# Create your views here.

def summary(request):
    api_key = "d44057b15d624d1e91583148251809"
    weather_data = None
    forecast_data = None
    user_city = None
    
    if request.method == 'POST':
        formdata = cityForm(request.POST)
        if formdata.is_valid():
            user_city = formdata.cleaned_data['city']
            
            # Get current weather
            response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_city}&aqi=no")
            if response.status_code == 200:
                weather_data = response.json()
            
            # Get forecast data (3 days by default)
            forecast_response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={user_city}&days=3&aqi=no")
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()
        
        return render(request, 'weatherapp/summary.html', {
            'form': cityForm, 
            'city': user_city, 
            'weather': weather_data,
            'forecast': forecast_data
        })

    return render(request, 'weatherapp/summary.html', {'form': cityForm})


def forecast(request):
    """Get weather forecast for the next 3, 5, or 10 days"""
    api_key = "d44057b15d624d1e91583148251809"
    forecast_data = None
    user_city = None
    
    if request.method == 'POST':
        formdata = cityForm(request.POST)
        if formdata.is_valid():
            user_city = formdata.cleaned_data['city']
            days = request.POST.get('days', 3)  # Default to 3 days
            
            # Get forecast data (supports 1-10 days)
            response = requests.get(
                f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={user_city}&days={days}&aqi=no"
            )
            
            if response.status_code == 200:
                forecast_data = response.json()
    
    return render(request, 'weatherapp/forecast.html', {
        'form': cityForm, 
        'city': user_city, 
        'forecast': forecast_data
    })


def alldata(request):
    return render(request, 'weatherapp/alldata.html', {'form': cityForm})
