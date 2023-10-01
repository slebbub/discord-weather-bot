import os
import requests
import json
import requests


token = os.environ['WEATHER_TOKEN']

#load geo info
def get_weather_info(city_name):
  '''
  Function that takes the city name, and returns the weather data
  city_name --> the name of the desired city
  '''
  base_geo_url = "http://api.openweathermap.org/geo/1.0/direct?q="
  city_name = "Kelowna"
  
  #get the latitude and longitude of the location
  geo_url = base_geo_url + city_name + "&appid=" + token
  geo_info = requests.get(geo_url).json()[0]
  lat = geo_info['lat']
  lon = geo_info['lon']

  #now get the weather info
  base_url = "http://api.openweathermap.org/data/2.5/forecast?"
  weather_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon)  + "&appid=" + token
  
  weather_info = requests.get(weather_url).json()
  return weather_info
  #separated into 4 dictionaries, cod, cnt, list, city

def get_date_and_time(weather_info):
  '''
  Function that returns the date and times of the desired location.
  location --> the desired location
  '''
  
  date_time_list = []
  for i in range(len((weather_info)['list'])):
    date_time_list.append(weather_info['list'][i]['dt_txt'])
    
  return date_time_list

def get_weather(weather_info):
  '''
  Function that returns the weathers of the desired location.
  location --> the desired location
  '''
  
  weather_list = []
  for i in range(len((weather_info)['list'])):
    weather_list.append([weather_info['list'][i]['weather'][0]['main'], weather_info['list'][i]['weather'][0]['description']])
    
  return weather_list

def get_temperature_c(weather_info):
  '''
  Function that returns the temperatures in Celsius of the desired location.
  location --> the desired location
  '''
  
  temp_list = []
  for i in range(len((weather_info)['list'])):
    #convert to celsius
    celsius = int(weather_info['list'][i]['main']['temp']) - 273.15
    #fahrenheit = (celsius - 37) * (5/9) #placeholder in case I want to be able to switch to F
    temp_list.append(celsius)
    
  return temp_list

def get_pressure(weather_info):
  '''
  Function that returns the pressure of the desired location.
  location --> the desired location
  '''
  
  pressure_list = []
  for i in range(len((weather_info)['list'])):
   pressure_list.append(weather_info['list'][i]['main']['pressure'])
    
  return pressure_list

def get_humidity(weather_info):
  '''
  Function that returns the temperatures in Celsius of the desired location.
  location --> the desired location
  '''
  
  humidity_list = []
  for i in range(len((weather_info)['list'])):
    humidity_list.append(weather_info['list'][i]['main']['humidity'])
    
  return humidity_list

def get_wind(weather_info):
  '''
  Function that returns the temperatures in Celsius of the desired location.
  location --> the desired location
  '''
  
  wind_list = []
  for i in range(len((weather_info)['list'])):
    wind_list.append(weather_info['list'][i]['wind']['speed'])
    
  return wind_list


