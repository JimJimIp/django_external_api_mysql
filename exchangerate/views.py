from django.shortcuts import render
from .models import Exchangerate

import requests
# import urllib3.request
# Create your views here.


def get_exchangerate():
    url = 'https://api.hkma.gov.hk/public/market-data-and-statistics/monthly-statistical-bulletin/er-ir/er-eeri-daily?offset=0'

    # response = requests.get(url)
    # data = response.json()["records"]
    
    response = requests.get(url)
    data = response.json()
    
    # data = requests.get(url).json()
    # print(data)
    
    for er in data:
    	# print("End of Day: " + er["end_of_day"])
        print(er) 
    	# print("US$: " + er["usd"])
        # print("OLED Display: " + str(k["oled_display"]))
    
    #? for er in data:
        #? if not Exchangerate.objects.filter(end_of_day=er["end_of_day"]).exists():
        
        #? Exchangerate.objects.create(usd=er["usd"], cny=er["cny"], jpy=er["jpy"], cad=er["cad"], aud=er["aud"], sgd=er["sgd"], thb=er["thb"], myr=er["myr"], eur=er["eur"])
        #? print("saved")
        
        #? else:
            #? print("have exists")