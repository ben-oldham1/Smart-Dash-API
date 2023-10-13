from tracemalloc import stop
from flask import Flask, Response, jsonify
import requests
import time

from data_gathering.busData import getBusData
from data_gathering.internetSpeed import getInternetSpeed
from data_gathering.weatherData import getWeatherData
from data_gathering.newsData import getNewsData

api = Flask(__name__)


# Bus information
@api.route('/busdata/<stopname>', methods=['GET'])
def busData(stopname):

    #try:
    busData = getBusData(stopname)
    #except:
        #print('Error retriving bus data')
        #return Response(status=500)

    return busData


# Internet speed test
@api.route('/speedtest', methods=['GET'])
def internetSpeed():

    try:
        speedData, records = getInternetSpeed()
    except:
        print('Error retriving speed data')
        return Response(status=500)
    
    print('request processed')
    return jsonify(speedData, records)


@api.route('/weather', methods=['GET'])
def get_weather():
    try:
        weatherData = getWeatherData()
        return jsonify(weatherData), 200
    except:
        return Response(status=500)

@api.route('/news', methods=['GET'])
def get_news():
    try:
        newsData = getNewsData()
        return jsonify(newsData), 200
    except:
        return Response(status=500)

 
if __name__ == '__main__':
    api.run(debug=True)