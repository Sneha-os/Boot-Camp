import tkinter as tk
import requests
from datetime import datetime

def getWeather(canvas):
    api_key = 'aa4223656f0d2e7299c5140a49b6cbfb'
    location = textfield.get()  
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
    api_data = requests.get(complete_api_link).json()

    temp_city = int(api_data['main']['temp'] - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    final_info = "Weather Stats for - \n{}   ||   {}".format(location.upper(), date_time)
    final_data = "\n" + weather_desc + "\n" + str(temp_city) + " degree C"
    final_data2 = "\n" + "Current Humidity: " + str(hmdt) + "%" + "\n" + "Current Wind speed: " + str(wind_spd) + "kmph"
    label1.config(text = final_info)
    label2.config(text = final_data)
    label3.config(text = final_data2)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins",15,"bold")
t = ("poppins",25,"bold")
k = ("Times",35,"bold italic")

textfield = tk.Entry(canvas, justify='center', width=20, font = k)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = k)
label1.pack()
label2 = tk.Label(canvas, font = t)
label2.pack()
label3 = tk.Label(canvas, font = f)
label3.pack()
canvas.mainloop()




