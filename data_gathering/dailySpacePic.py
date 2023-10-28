import requests

# Call the NASA API
def getDailySpacePic():

    # Make a request to the NASA daily space pic API
    apiUrl = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2023-10-12"
    response = requests.get(apiUrl)
    data = response.json()

    # Return the weather data as a JSON response
    return data