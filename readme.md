# Smart Dashboard API

This repo contains the backend API for my smart dashboard API. You can view the main project [here](https://github.com/ben-oldham1/Smart-Dash-Frontend)

# Endpoints

| Endpoint | Purpose |
| --- | --- |
| `/busdata/<stopname>` | Given the name of a bus stop, returns the upcoming bus departures from that stop |
| `/speedtest` | Calculates and returns internet speed data |
| `/weather` | Returns weather data from external API |

# Functions

## Bus data
This function scrapes publicly available data on live bus departures from a given stop. It returns the data in JSON format.

## Internet speed
Uses the [speedtest python library](https://github.com/sivel/speedtest-cli/wiki) to get the upload and download speeds.

## Internet speed
Returns weather data fetched from the OpenWeatherMap API. 
