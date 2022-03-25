# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    '''Look for a given city and disambiguate between several candidates.
    Returns one city (or None)'''

    url = BASE_URI + "/api/location/search/"
    payload = {"query" : query}
    response = requests.get(url, payload ).json()
    city_data = None
    if len(response) > 0:
        city_data = response[0]

    return city_data


def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''
    url = BASE_URI + f"/api/location/{woeid}/"
    response = requests.get(url).json()
    weather_data = response["consolidated_weather"][1:] #Take the next 5 days weather
    return weather_data


def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)


    try:
        print(f"Here's the weather in {city['title']}")
        forecast_data = weather_forecast(city['woeid'])
        for i in forecast_data:
            print(
                f"{i['applicable_date']}: {i['weather_state_name']} {round(i['the_temp'],1)}°C "
            )


    except:
        print(city)

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
