import requests

def get_weather(city):
    API_KEY = "585de1b98bf86105b74e2114593bad06"  # Replace with your working key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        print(f"\n📍 Weather in {city.title()}:\n🌡️ Temperature: {temperature}°C\n💧 Humidity: {humidity}%\n🌥️ Condition: {weather.capitalize()}")
    else:
        print("\n🚫 City not found. Please enter a valid city name.")

if __name__ == "__main__":
    print("🌦️ Welcome to Python Weather CLI 🌦️")
    city_name = input("Enter a city name: ")
    get_weather(city_name)
