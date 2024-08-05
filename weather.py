from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from tkinter import messagebox

def get_weather(city, textfield, clock, name, labels):
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(city)
        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            
            # Display time 
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

            # Get weather information
            api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=36d9154e86383f879449bdce9cf7d652"
            response = requests.get(api).json()

            if response.get("cod") == 200:
                weather_description = response["weather"][0]["description"]
                temperature = response["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
                pressure = response["main"]["pressure"]
                humidity = response["main"]["humidity"]
                wind_speed = response["wind"]["speed"]
                
                labels["description"].config(text=weather_description)
                labels["humidity"].config(text=f"{humidity} %")
                labels["pressure"].config(text=f"{pressure} hPa")
                labels["wind"].config(text=f"{wind_speed} m/s")
            else:
                messagebox.showerror("Error", "Cannot find weather information for this city!")
        else:
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


