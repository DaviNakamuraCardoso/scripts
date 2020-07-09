#! /usr/bin/python3

import requests
import json
import sys
import pprint


# JSON_weather - prints the weather for a location from the command line.
# Compute location from command line arguments
location = input('Local: ')
apiid = 'ab72eafe8c2d81656e13dba00ebba215'

json_file = open('city.txt', 'r')
json_con = json_file.read()
py_data = json.loads(str(json_con))

# Getting the city id

print('Checking the city id...')
ndict = {}
for dict in py_data:
    ndict[dict['name']] = dict['id']

json_file.close()


print("Dowloading the JSON data from OpenWeatherMap.org's API...")

url = 'https://api.openweathermap.org/data/2.5/forecast?id=%s&APPID=%s' % (ndict[location], apiid)

response = requests.get(url)
response.raise_for_status()
weather_data = json.loads(response.text)

w = weather_data['list']
print('Current weather in %s:' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow: ')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
