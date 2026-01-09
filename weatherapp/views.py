from django.shortcuts import render
import requests
from .forms import cityForm
from django.conf import settings
# Create your views here.

def summary(request):
    api_key = "d44057b15d624d1e91583148251809"
    if request.method == 'POST':
        formdata = cityForm(request.POST)
        if formdata.is_valid():
            user_city = formdata.cleaned_data['city']

        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_city}&aqi=no")
        return render(request, 'weatherapp/summary.html', {'form': cityForm, 'city': user_city, 'weather': response.json()})

    return render(request, 'weatherapp/summary.html', {'form': cityForm})


def alldata(request):
    return render(request, 'weatherapp/alldata.html', {'form': cityForm})
