import requests

# Import the credentials.py file, containing API keys, etc
import credentials

# Call the NASA API
def getDailySpacePic():

    # Make a request to the NASA daily space pic API
    apiUrl = f"https://api.nasa.gov/planetary/apod?api_key={credentials.nasaSpaceAPIkey}"
    response = requests.get(apiUrl)
    data = response.json()

    # Return the weather data as a JSON response
    return data