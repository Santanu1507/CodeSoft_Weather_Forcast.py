# Weather Forecast App

The Weather Forecast App is a graphical application built using the Tkinter library in Python. It provides real-time weather information for a given location using the OpenWeatherMap API. The app displays temperature, humidity, wind speed, weather description, country, and visibility. The graphical user interface (GUI) is designed with a colorful and user-friendly layout.

## Features

- Retrieve weather data for a specified location.
- Display temperature in Celsius.
- Show humidity and wind speed in meters per second.
- Provide a description of the current weather conditions.
- Show the country based on the city name using the geopy library.
- Display visibility in meters.
- Custom fonts and background colors for an appealing user interface.

## Requirements

- Python 3.x
- Tkinter library
- Requests library
- Geopy library

## Usage

1. Run the script using Python.
2. The main window of the Weather Forecast App will open.
3. Enter the name of the city or location for which you want to get weather information in the "Enter Location" field.
4. Click the "Get Weather" button to fetch the weather details.
5. The app will display the weather information for the specified location, including temperature, humidity, wind speed, weather description, country, and visibility.

## Error Handling

- If the city or location entered is not found, an error message will be displayed.
- If there is a connection error or an error fetching data from the server, appropriate error messages will be shown.

## Note

- The app uses the OpenWeatherMap API to fetch weather data. Please ensure you have an active internet connection to access the API.

## Customization

- You can customize the background color, font styles, and layout of the app to suit your preferences.
- If you wish to change the API key or base URL for weather data, you can modify the `api_key` and `base_url` variables in the code.

Feel free to explore and enhance the app as per your requirements. Enjoy checking the weather with this simple and user-friendly Weather Forecast App!
