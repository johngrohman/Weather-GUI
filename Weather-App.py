import tikinter as tk
import requests
from datetime import date
import tkinter.font

CANVAS_HEIGHT = 700
CANVAS_WIDTH = 1200

today = date.today()

current_date = today.strftime('%B %d, %Y')

def get_weather(city):
    weather_key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()
    print(weather)

    city_label['text'] = weather['name']
    current_temp['text'] = weather['main']['temp']
    high_low['text'] = str(weather['main']['temp_max']) + ' / ' + str(weather['main']['temp_min'])

