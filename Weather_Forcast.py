# Import necessary libraries
import requests
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim

# Function to get weather information
def get_weather():
    api_key = "c9140ef105b8f16fba798ffc1f98f1cc"  
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    
    # Get the city name from the entry field
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city or location.")
        return
    
    # Set the parameters for the weather API request
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        # Send the API request and get the response
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the response code is 200 (success)
        if data["cod"] == 200:
            # Extract weather information from the response
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            weather_desc = data["weather"][0]["description"].capitalize()
            weather_icon = data["weather"][0]["icon"]
            visibility = data.get("visibility", "N/A")

            # Set the weather icon image
            icon_url = f"http://openweathermap.org/img/w/{weather_icon}.png"
            response_icon = requests.get(icon_url)
            with open("weather_icon.png", "wb") as f:
                f.write(response_icon.content)

            # Display the weather icon
            weather_icon_img = tk.PhotoImage(file="weather_icon.png")
            weather_icon_label.config(image=weather_icon_img)
            weather_icon_label.image = weather_icon_img  # Keep a reference to the image

            # Get the country based on the city name using geopy's Nominatim
            geolocator = Nominatim(user_agent="weather_app")
            location = geolocator.geocode(city)
            if location:
                country_code = location.raw.get("display_name", "N/A")
            else:
                country_code = "N/A"

            # Update the result_label text with weather information
            result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nWeather: {weather_desc}\nCountry: {country_code}\nVisibility: {visibility} meters", wraplength=350)

        else:
            # Show an error message if the city is not found
            messagebox.showerror("Error", "City not found!")
    except requests.ConnectionError:
        # Show an error message if there's a connection error
        messagebox.showerror("Error", "Connection Error. Please check your internet connection.")
    except requests.RequestException:
        # Show an error message if there's an error fetching data from the server
        messagebox.showerror("Error", "Error fetching data from the server.")
    except Exception as e:
        # Show a generic error message for other exceptions
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
app = tk.Tk()
app.title("Weather Forecast App")
app.geometry("650x500")  # Set the initial window size to 650x500

app.configure(bg="#d94d1e")  # Set the background color of the main window to a reddish shade (#d94d1e)

# Custom fonts
font_style = ("Comic Sans MS", 12)

# Create and pack widgets for the GUI
city_label = tk.Label(app, text="Enter Location", font=font_style, bg="#d94d1e")  # Change the label background to reddish shade (#d94d1e)
city_label.pack(pady=10)

city_entry = tk.Entry(app, font=font_style, bg="#ffe082")  # Change the entry background to a lighter yellow (#ffe082)
city_entry.pack()

get_weather_btn = tk.Button(app, text="Get Weather", command=get_weather, font=font_style, bg="#a8579d", fg="white")  # Change the button background to a purplish shade (#a8579d)
get_weather_btn.pack(pady=10)

weather_icon_label = tk.Label(app, bg="#d94d1e")  # Change the icon label background to reddish shade (#d94d1e)
weather_icon_label.pack(pady=10)

result_label = tk.Label(app, text="", font=font_style, bg="#d94d1e", wraplength=350)  # Change the result label background to a greenish shade (#a5d6a7)
result_label.pack(pady=10)

app.mainloop()
