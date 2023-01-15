from django.shortcuts import render
from main.models import Population

import requests
# Create your views here.


def get_population():
    
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

    response = requests.get(url)
    data = response.json()["data"]
    print(data)
    
    for country in data:
        if not Population.objects.filter(country=country["Nation"], year=country["Year"]).exists():
        
            Population.objects.create(country=country["Nation"], year=country["Year"], human_count=country["Population"])
            print("saved")
        
        else:
            print("have exists")
    