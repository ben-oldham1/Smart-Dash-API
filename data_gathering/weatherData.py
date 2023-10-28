import requests
import datetime

# Import the credentials.py file, containing API keys, etc
import credentials

# Get the main weather data
def callWeatherAPI():
    # Retrieve the required parameters from the request
    apiKey = credentials.weatherAPIkey
    city = credentials.weatherCity
    country = credentials.weatherCountry

    # Make a request to the OpenWeatherMap API
    apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={apiKey}&units=metric"
    response = requests.get(apiUrl)
    data = response.json()

    # Format temperature and wind values to one decimal place
    if 'main' in data:
        data['main']['temp'] = round(data['main']['temp'], 1)
        data['main']['feels_like'] = round(data['main']['feels_like'], 1)
        data['wind']['speed'] = round(data['wind']['speed'], 1)

        data['sys']['sunrise'] = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
        data['sys']['sunset'] = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')

    # Return the weather data as a JSON response
    return data

# Get the main weather data
def getWeatherData():
    data = callWeatherAPI()

    return data

# Get the sunrise and sunset data
def getSunCycleData():
    data = callWeatherAPI()

    suncycle = {
        'sunrise': data['sys']['sunrise'],
        'sunset': data['sys']['sunset']
    }

    return suncycle
