import requests
import os
from datetime import datetime

def weather(location):
    user_api = "a6560fd9942772cf838c5e9a0e2d08cd"

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        print("Invalid City.")
    else:
        temp_city = int((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']

    weather_list = [temp_city, weather_desc]

    return weather_list
