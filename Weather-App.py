#!/usr/bin/python

import tkinter as tk
import requests
from datetime import date
from Converter import converter_function

CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500

today = date.today()

current_date = today.strftime('%B %d, %Y')

class City:
    def __init__(self, name: str,
    current_temp: int,
    description,
    wind_speed,
    high,
    low,
    pressure,
    humidity):
        self.name = name
        self.current_temp = current_temp
        self.description = description
        self.wind_speed = wind_speed
        self.high = high
        self.low = low
        self.pressure = pressure
        self.humidity = humidity
        self.units = 'F'

    def convert_units(self):
        if self.units == 'F':
            self.units = 'C'
        else:
            self.units = 'F'
        for temp in temperatures:
            pass
        self.temp = converter_function(self.temp, self.units)

def get_weather(city):
    weather_key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()
    print(weather)
    print(weather['weather'])
    # if weather.get('message') == 'city not found':
    #     city_label = 'Unknown'
    # else:
    city = City(weather['name'],
    weather['main']['temp'],
    weather['weather'][0]['description'],
    weather['wind']['speed'],
    weather['main']['temp_max'],
    weather['main']['temp_min'],
    weather['main']['pressure'],
    weather['main']['humidity'])

    convert = tk.Button(top_frame, bd = 0, text = 'F/C', bg = 'blue', command = lambda: city.convert_units())
    convert.place(relx = 0, relwidth = .1, relheight = .9, rely = .05)
    city_label['text'] = city.name
    current_temp['text'] = city.current_temp
    description['text'] = city.description
    wind_speed['text'] = city.wind_speed
root = tk.Tk()

canvas = tk.Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH, bg = '#f9f7f7')
canvas.pack()

# Top Bar
top_frame = tk.Frame(root, bg = 'red', bd = 5)
top_frame.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.1)

city_label = tk.Label(top_frame, bg = 'purple')
city_label.place(relx = .1, relwidth = .4, relheight = 1, rely = .1)
city_label.config(font=('Helvetica', 30))

entry = tk.Entry(top_frame, font = 40, bg = 'green', bd = 0, state = 'normal')
entry.place(relx = .5, relheight = 1, relwidth = .3)

search = tk.Button(top_frame, bd = 0, text = "Search", bg = 'blue', command = lambda: get_weather(entry.get()))
search.place(relx = .8, relwidth = .2, relheight = .9, rely = .05)

# Left Block
left_frame = tk.Frame(root, bg = 'blue', bd = 5)
left_frame.place(relx = 0.05, rely = .19, relwidth = .445, relheight = .75)

# Current temp
current_temp = tk.Label(left_frame, bg = 'red')
current_temp.place(relx = .01, relwidth = .98, relheight = .45, rely = .01)
current_temp.config(font = ('Helvetica', 30))
# Description

description = tk.Label(left_frame, bg = 'red')
description.place(relx = .01, relwidth = .98, relheight = .25, rely = .48)
description.config(font = ('Helvetica', 20))
# Wind Speed
wind_speed = tk.Label(left_frame, bg = 'red')
wind_speed.place(relx = .01, relwidth = .98, relheight = .25, rely = .75)
wind_speed.config(font = ('Helvetica', 20))


# Right Block
right_frame = tk.Frame(root, bg = 'orange', bd = 5)
right_frame.place (relx = .525, rely = .19, relwidth = .425, relheight = .75)

# High

# Low

# Pressure

# Humidity

root.mainloop()
