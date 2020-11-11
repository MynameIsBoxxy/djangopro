from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
   # appid = '439d4b804bc8187953eb36d2a8c26a02'
    appid = '1bd58ba858af0cf39e8c25b5957e5b12'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        
        r = requests.get(url.format(city.name)).json()
        
        city_info = {
            'city': city.name,
            'temp': r["main"]["temp"],
            'icon': r["weather"][0]["icon"],
        }
        all_cities.append(city_info)
        
    
    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)