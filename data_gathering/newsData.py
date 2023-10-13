import requests

# Import the credentials.py file, containing API keys, etc
import credentials
from data_gathering.busData import getBusData

def getNewsData():
    # Retrieve the required parameters from the request
    apiKey = credentials.newsAPIkey

    # Set some parameters for the API request
    language = 'en'
    country = 'gb'
    numArticles = '5'

    # Make a request to the NewsData.io API
    apiUrl = f"https://newsdata.io/api/1/news?apikey={apiKey}&language={language}&size={numArticles}&country={country}"
    response = requests.get(apiUrl)
    data = response.json()

    print('News data fetched')

    # Return the weather data as a JSON response
    return data