import requests

# Import the credentials.py file, containing API keys, etc
import credentials
from data_gathering.busData import getBusData

def getNewsData():
    # Retrieve the required parameters for the request
    apiKey = credentials.newsAPIkey
    language = credentials.newsLanguage
    country = credentials.newsCountry
    numArticles = credentials.newsNumArticles

    # Make a request to the NewsData.io API
    apiUrl = f"https://newsdata.io/api/1/news?apikey={apiKey}&language={language}&size={numArticles}&country={country}"
    response = requests.get(apiUrl)
    data = response.json()

    print('News data fetched')

    # Return the weather data as a JSON response
    return data