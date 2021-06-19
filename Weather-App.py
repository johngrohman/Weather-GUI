import tkinter as tk
import requests
from datetime import date
import tkinter.font

CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500

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

root = tk.Tk()

canvas = tk.Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH, bg = '#f9f7f7')
canvas.pack()

# Date
date_frame = tk.Frame(root, bg = '#dbe2ef', bd = 5)
date_frame.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.1)


go_button = tk.Button(root, bd = 0, text = "Go", bg = '#dbe2ef', command = lambda: get_weather(entry.get()))
go_button.place(relx = .82, relwidth = .16, rely = .1)


root.mainloop()
