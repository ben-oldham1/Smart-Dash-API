import requests
from datetime import datetime

stopData = {
    'UWE-SB': '0170SGP90686',
    'UWE-NB': '0170SGP90685',
    'stoke-SB': '0170SGP90680',
    'centre-NB': '0100BRP90372',
    'cabot-NB': '0100BRA01798'
}

def getBusData(stopName):
    # Lookup the stop ID from its name
    stopID = stopData[stopName]

    response = requests.get("https://journeyplanner.travelwest.info/api/idox/?stopID="+ stopID +"&maxItems=8&lookAheadMinutes=180")
    response = response.json()

    busData = {
        'alerts': '',
        'buses': []
    }

    # Extract any alerts about disruption
    if 'lineNotice' in response['data']:
        busData['alerts'] = response['data']['lineNotice']

    # Extract the bus data
    response = response['data']['rtiReports'][0]['upcomingCalls']

    for bus in response:
        busData['buses'].append({
            'headsign': bus['tripInfo']['headsign'],
            'lineName': bus['routeInfo']['lineName'],
            'scheduledDepartureTime': datetime.strptime(bus['scheduledCall']['scheduledDepartureTime'], '%Y-%m-%dT%H:%M:%S%z').strftime('%H:%M'),
        })

    return busData