# weather_module.py

import requests
from tts_module import speak
from my_config import OPENWEATHER_API_KEY

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            condition = data['weather'][0]['description']
            weather_report = f"The current temperature in {city} is {temp}°C with {condition}."
            print(weather_report)
            speak(weather_report)
        elif response.status_code == 401:
            print("Invalid API key. Please check your API key in my_config.py.")
            speak("Sorry, I couldn't get the weather. Invalid API key.")
        elif response.status_code == 404:
            print(f"City '{city}' not found.")
            speak(f"Sorry, I couldn't find the weather for {city}.")
        else:
            print("Sorry, I couldn't get the weather right now.")
            speak("Sorry, I couldn't get the weather right now.")
    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")
        speak("Sorry, I couldn't get the weather due to a network error.")

