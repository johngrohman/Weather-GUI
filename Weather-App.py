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
        self.units = 'F'

    def convert_units(self):
        if self.units == 'F':
            self.units = 'C'
        else:
            self.units = 'F'
        self.temp = converter_function(self.temp, self.units)

def get_weather(city):
    weather_key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()

    if weather.get('message') == 'city not found':
        city_label = 'Unknown'
    else:
        city = City_Weather(weather.get('name'), weather['main']['temp'])
        convert = tk.Button(top_frame, bd = 0, text = 'F/C', bg = 'blue', command = lambda: city.convert_units())
        convert.place(relx = 0, relwidth = .1, relheight = .9, rely = .05)

root = tk.Tk()

canvas = tk.Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH, bg = '#f9f7f7')
canvas.pack()

# Top Bar
top_frame = tk.Frame(root, bg = 'red', bd = 5)
top_frame.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.1)

entry = tk.Entry(top_frame, font = 40, bg = 'green', bd = 0, state = 'normal')
entry.place(relx = .5, relheight = 1, relwidth = .3)

search = tk.Button(top_frame, bd = 0, text = "Search", bg = 'blue', command = lambda: get_weather(entry.get()))
search.place(relx = .8, relwidth = .2, relheight = .9, rely = .05)



root.mainloop()
