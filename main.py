from flask import Flask, Response, jsonify

from data_gathering.busData import getBusData
from data_gathering.internetSpeed import getInternetSpeed
from data_gathering.weatherData import getWeatherData, getSunCycleData
from data_gathering.newsData import getNewsData
from data_gathering.dailySpacePic import getDailySpacePic

api = Flask(__name__)


@api.route('/busdata/<stopname>', methods=['GET'])
def busData(stopname):

    try:
        busData = getBusData(stopname)
    except:
        print('Error retriving bus data')
        return Response(status=500)

    return busData

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
        print('Error retriving weather data')
        return Response(status=500)

@api.route('/suncycle', methods=['GET'])
def get_suncycle():
    try:
        SunCycleData = getSunCycleData()

        return jsonify(SunCycleData), 200
    except:
        print('Error retriving sun cycle data')
        return Response(status=500)

@api.route('/news', methods=['GET'])
def get_news():
    try:
        newsData = getNewsData()
        return jsonify(newsData), 200
    except:
        print('Error retriving news data')
        return Response(status=500)

@api.route('/dailyspacepic', methods=['GET'])
def get_dailyspacepic():
    try:
        dailySpacePic = getDailySpacePic()
        return jsonify(dailySpacePic), 200
    except:
        print('Error retriving space pic data')
        return Response(status=500)

 
if __name__ == '__main__':
    api.run(debug=True)