# pylint: disable=missing-docstring,invalid-name

# TODO: paste the code from Kitt's instructions

import requests
import sys

url = "https://www.metaweather.com/api/location/search/?query=london"
response = requests.get(url).json()
city = response[0]
print(type(city['woeid']))
print(f"{city['title']}: {city['woeid']} ({city['latt_long']})")
