from tracemalloc import stop
from flask import Flask, Response, jsonify
import requests
import time

from busData import getBusData
from internetSpeed import getInternetSpeed
from weatherData import getWeatherData

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
        print('Error retriving bus data')
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


 
if __name__ == '__main__':
    api.run(debug=True)