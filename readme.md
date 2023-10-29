<div align="center">
  <img alt="Logo" src="https://github.com/ben-oldham1/Smart-Dash-Frontend/blob/cb40692ebebf2619e1dab22bc70e268fec19ff87/public/logo512.png" width="100" />
</div>
<h1 align="center">
  Smart Dashboard (backend)
</h1>
<p align="center">
The backend for my smart dashboard project. It provides an API for the <a href="https://github.com/ben-oldham1/Smart-Dash-Frontend">frontend</a> to call. 
</p>
<p  align="center">
<img  src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
</p>
 	

## Basic outline

The `main.py` file contains the Flask API endpoints. It calls the functions that return the requested data, or returns an error message. 

### Data gathering functions

A variety of functions gather data for the API to return. They are located in the specified file in the `/data_gathering` directory.

| Function | Location | Purpose |
| --- | --- | --- |
| `getBusData(stopName)` | `busData.py` | Given the name of a bus stop, returns the upcoming bus departures from that stop. |
| `getDailySpacePic()` | `dailySpacePic.py` | Calls the NASA daily space pic API and returns the response. |
| `loadDataFromJSON(file_path)` | `internetSpeed.py` | Loads data from a JSON file (specified by the file_path), returning the data if the file exists, or an empty list if not. |
| `saveDataToJSON(file_path, data)` | `internetSpeed.py` | Saves the provided data to a JSON file specified by the file_path. |
| `getInternetSpeed()` | `internetSpeed.py` | Measures the current internet speed using the `speedtest` library, records the test results and time in a JSON file, and returns the last 8 results. |
| `getNewsData()` | `newsData.py` | Fetches the latest headlines from the **newsdata.io** API and returns them. |
| `callWeatherAPI()` | `weatherData.py` | Makes a call to the the **OpenWeatherMap** API and returns the whole response data. |
| `getWeatherData()` | `weatherData.py` | A wrapper function that calls `callWeatherAPI()` and returns all the data. |
| `getSunCycleData()` | `weatherData.py` | A wrapper function that calls `callWeatherAPI()` and returns the sunset and sunrise data. |

## Roadmap
- A caching system will be implemented, so API calls can be made and saved to a file on a regular schedule, preventing the need to call each api every time the front-end requests data. This will improve scalability and performance.
