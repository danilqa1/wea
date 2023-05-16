import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm



def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=680a3ba6291adcd3cbd9c0d68dd23a35'
    
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
        
    form = CityForm()
    
    cities = City.objects.all()
    
    all_cities = []
    
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }
        
        all_cities.append(city_info)
    
    context = {'all_info': all_cities, 'form': form} 
    
    return render(request, 'weather/index.html', context)


def delete_data(request, name):
     form = CityForm()
     cities = City.objects.all().filter(name=name)
     cities.delete()
     return render(request, 'weather/index.html', context)