import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "585de1b98bf86105b74e2114593bad06"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Oops!", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        messagebox.showerror("Error", f"City '{city}' not found.")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    result_label.config(
        text=f"📍 {city.title()}\n🌡️ Temp: {temp}°C\n💧 Humidity: {humidity}%\n🌥️ {condition.capitalize()}"
    )

# GUI setup
root = tk.Tk()
root.title("Weather App 🌦️")
root.geometry("300x250")
root.resizable(False, False)

title = tk.Label(root, text="🌍 Weather App", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Helvetica", 12))
city_entry.pack(pady=5)
city_entry.insert(0, "Enter city")

get_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="center")
result_label.pack(pady=10)

root.mainloop()
