#!/usr/bin/python

import tkinter as tk
import requests
from datetime import date
from Converter import converter_function

CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500

today = date.today()

current_date = today.strftime('%B %d, %Y')

class City_Weather:
    def __init__(self, name: str, temp: int):
        self.name = name
        self.temp = temp

    def convert_units(self, unit: str):
        if unit == 'F':
            self.units = 'F'
        else:
            self.units = 'C'
        self.temp = converter_function(self.temp, unit)

def get_weather(city):
    weather_key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()
    print(weather)

    if weather.get('message') == 'city not found':
        city_label = 'Unknown'
    else:
        city_label = weather.get('name')

        city = City_Weather(weather.get('name'))

    print('city_label: ', city_label)



root = tk.Tk()

canvas = tk.Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH, bg = '#f9f7f7')
canvas.pack()

# Search Bar
search_frame = tk.Frame(root, bg = 'red', bd = 5)
search_frame.place(relx = 0.45, rely = 0.05, relwidth = 0.5, relheight = 0.1)

entry = tk.Entry(search_frame, font = 40, bg = 'green', bd = 0, state = 'normal')
entry.place(relheight = 1, relwidth = .7)

search = tk.Button(search_frame, bd = 0, text = "Search", bg = 'blue', command = lambda: get_weather(entry.get()))
search.place(relx = .7, relwidth = .3, relheight = .9, rely = .05)

# root.mainloop()
