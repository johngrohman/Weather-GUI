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
    def __init__(self,
    name,
    current_temp,
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
        elif self.units == 'C':
            self.units = 'F'

        self.current_temp = converter_function(self.current_temp, self.units)
        current_temp = tk.Label(left_frame, bg = '#D8973C', text = 'Current \nTemperature: \n' + str(int(self.current_temp))+ '°' + self.units)
        current_temp.place(relx = .01, relwidth = .98, relheight = .45, rely = .01)
        current_temp.config(font = ('Helvetica', 30))

        self.high = converter_function(self.high, self.units)
        high = tk.Label(right_frame, bg = '#D8973C', text = 'High: ' + str(int(self.high))+ '°' + self.units)
        high.place(relx = .01, relwidth = .98, relheight = .20, rely = .01)
        high.config(font = ('Helvetica', 20))

        self.low = converter_function(self.low, self.units)
        low = tk.Label(right_frame, bg = '#D8973C', text = 'Low: ' + str(int(self.low))+ '°' + self.units)
        low.place(relx = .01, relwidth = .98, relheight = .20, rely = .24)
        low.config(font = ('Helvetica', 20))

def get_weather(city, units):
    weather_key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()
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
    current_temp['text'] = 'Current \nTemperature: \n' + str(int(city.current_temp))+ '°' + city.units
    description['text'] = 'Description: \n' + str(city.description)
    wind_speed['text'] = 'Wind Speed: ' + str(int(city.wind_speed))
    high['text'] = 'High: ' + str(int(city.high))+ '°' + city.units
    low['text'] = 'Low: ' + str(int(city.low))+ '°' + city.units
    pressure['text'] = 'Pressure: \n' + str(int(city.pressure)) + ' mb'
    humidity['text'] = 'Humidity: \n' + str(int(city.humidity)) + ' %'


root = tk.Tk()

canvas = tk.Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH, bg = '#D8C99B')
canvas.pack()

# Top Bar
top_frame = tk.Frame(root, bg = '#A4243B', bd = 5)
top_frame.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.1)

city_label = tk.Label(top_frame, text = 'City', bg = '#A4243B')
city_label.place(relx = .1, relwidth = .4, relheight = 1, rely = .1)
city_label.config(font=('Helvetica', 30))

entry = tk.Entry(top_frame, font = 40, bg = '#A4243B', bd = 0, state = 'normal')
entry.place(relx = .5, relheight = 1, relwidth = .3)

search = tk.Button(top_frame, bd = 0, text = "Search", command = lambda: get_weather(entry.get(), 'F'))
search.place(relx = .825, relwidth = .15, relheight = .9, rely = .05)

# Left Block
left_frame = tk.Frame(root, bg = '#A4243B', bd = 5)
left_frame.place(relx = 0.05, rely = .19, relwidth = .445, relheight = .75)

# Current temp
current_temp = tk.Label(left_frame, bg = '#D8973C', text = 'Current \nTemperature: \n')
current_temp.place(relx = .01, relwidth = .98, relheight = .45, rely = .01)
current_temp.config(font = ('Helvetica', 30))

# Description
description = tk.Label(left_frame, bg = '#D8973C', text = 'Description: \n')
description.place(relx = .01, relwidth = .98, relheight = .25, rely = .48)
description.config(font = ('Helvetica', 20))
# Wind Speed
wind_speed = tk.Label(left_frame, bg = '#D8973C', text = 'Wind Speed: ')
wind_speed.place(relx = .01, relwidth = .98, relheight = .25, rely = .75)
wind_speed.config(font = ('Helvetica', 20))


# Right Block
right_frame = tk.Frame(root, bg = '#A4243B', bd = 5)
right_frame.place (relx = .525, rely = .19, relwidth = .425, relheight = .75)

# High
high = tk.Label(right_frame, bg = '#D8973C', text = 'High: ')
high.place(relx = .01, relwidth = .98, relheight = .20, rely = .01)
high.config(font = ('Helvetica', 20))

# Low
low = tk.Label(right_frame, bg = '#D8973C', text = 'Low: ')
low.place(relx = .01, relwidth = .98, relheight = .20, rely = .24)
low.config(font = ('Helvetica', 20))

# Pressure
pressure = tk.Label(right_frame, bg = '#D8973C', text = 'Pressure: \n')
pressure.place(relx = .01, relwidth = .98, relheight = .25, rely = .48)
pressure.config(font = ('Helvetica', 20))

# Humidity
humidity = tk.Label(right_frame, bg = '#D8973C', text = 'Humidity: \n')
humidity.place(relx = .01, relwidth = .98, relheight = .25, rely = .75)
humidity.config(font = ('Helvetica', 20))

root.mainloop()

# get_weather('St. Louis')
