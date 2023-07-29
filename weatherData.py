from json.tool import main
from turtle import title
from flask import jsonify
import requests

def getWeatherData():
    # Retrieve the required parameters from the request
    apiKey = 'cadbd0ffe610d790aa93e83718ef070d'
    city = 'bristol'
    country = 'UK'

    # Make a request to the OpenWeatherMap API
    apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={apiKey}&units=metric"
    response = requests.get(apiUrl)
    data = response.json()

    # Format temperature and wind values to one decimal place
    if 'main' in data:
        data['main']['temp'] = round(data['main']['temp'], 1)
        data['main']['feels_like'] = round(data['main']['feels_like'], 1)
        data['wind']['speed'] = round(data['wind']['speed'], 1)

    # Return the weather data as a JSON response
    return data