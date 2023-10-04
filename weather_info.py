import os
import requests
import json
import requests

token = os.environ['WEATHER_TOKEN']


#load geo info
def get_weather_info(city_name, country):
  '''
  Function that takes the city name, and returns the weather data
  city_name --> the name of the desired city
  '''
  base_geo_url = "http://api.openweathermap.org/geo/1.0/direct?q="
  

  #get the latitude and longitude of the location
  geo_url = base_geo_url + city_name + ',' + country + "&appid=" + token
  geo_info = requests.get(geo_url).json()[0]
  lat = geo_info['lat']
  lon = geo_info['lon']

  #now get the weather info
  base_url = "http://api.openweathermap.org/data/2.5/forecast?"
  weather_url = base_url + "lat=" + str(lat) + "&lon=" + str(
      lon) + "&appid=" + token

  weather_info = requests.get(weather_url).json()
  location = weather_info['city']['name']
  country = weather_info['city']['country']
  
  return weather_info, location, country


def get_date_and_time(weather_info):
  '''
  Function that returns the date and times of the desired location.
  location --> the desired location
  '''

  date_time_list = []
  for i in range(len((weather_info)['list'])):
    date_time_list.append(weather_info['list'][i]['dt_txt'])

  return date_time_list


def get_full_weather(weather_info, timeframe): 
  '''
  Function that returns the full weather description of the desired location.
  Includes date & time, weather, detailed weather, temperature, humidity, pressure, and wind
  location --> the desired location
  timeframe --> the time to check [now|today|week]
  '''
  
  weather_list = []
  if timeframe == 'now':
    weather_list.append([
      weather_info['list'][0]['weather'][0]['main'],
      weather_info['list'][0]['weather'][0]['description'],
      weather_info['list'][0]['dt_txt'],
      weather_info['list'][0]['main']['temp'],
      weather_info['list'][0]['main']['pressure'],
      weather_info['list'][0]['main']['humidity'],
      weather_info['list'][0]['wind']['speed']
    ])
  elif timeframe == 'today':
      for i in range(8): #takes weather every 3 hours, so 8 gets the next 24hrs
        weather_list.append([
          weather_info['list'][i]['weather'][0]['main'],
          weather_info['list'][i]['weather'][0]['description'],
          weather_info['list'][i]['dt_txt'],
          weather_info['list'][i]['main']['temp'],
          weather_info['list'][i]['main']['pressure'],
          weather_info['list'][i]['main']['humidity'],
          weather_info['list'][i]['wind']['speed']
        ])
    
  elif timeframe == 'week':
    for i in range(len((weather_info)['list'])):
          weather_list.append([
            weather_info['list'][i]['dt_txt'],
            weather_info['list'][i]['weather'][0]['main'],
            weather_info['list'][i]['weather'][0]['description'],
            weather_info['list'][i]['main']['temp'],
            weather_info['list'][i]['main']['pressure'],
            weather_info['list'][i]['main']['humidity'],
            weather_info['list'][i]['wind']['speed']
          ])
  else:
    return 'error'
  return weather_list


def write_weather_statements(weather_list):
  statement_list = []
  for i in range(len(weather_list)):
    statement_list.append(f"Date: {weather_list[i][0]}"
                          f"Weather: {weather_list[i][1]}, {weather_list[i][2]}" 
                          f"Temperature: {weather_list[i][3]}"
                          f"Pressure: {weather_list[i][4]}"
                          f"Humidity: {weather_list[i][5]}"
                          f"Wind Speed: {weather_list[i][6]}"
    )
  return statement_list

#alert section
#triggers will be formatted as:
#  "[above|below] [value]" for numerical"
#  "[weather1],[weather2],...,[weathern]" for weather

def check_weather(weather_info, trigger):
  '''
  Function that checks the weather info and checks if a weather trigger has been hit
  
  weather_info --> weather info from api
  trigger --> [weather1],[weather2],...,[weathern]
  '''
  
  triggers = trigger.split(',')
  for i in range(len((weather_info)['list'])):
    main = weather_info['list'][i]['weather'][0]['main']
    details = weather_info['list'][i]['weather'][0]['description']
    if main in triggers or details in triggers:
      return 1
    else:
      return 0
    

def check_temperature_c(weather_info, trigger):
  '''
  Function that checks the weather info and checks if a temperature trigger has been hit
  
  weather_info --> weather info from api
  trigger --> [above|below] [value]
  '''

  temp_list = []
  for i in range(len((weather_info)['list'])):
    #convert to celsius
    celsius = int(weather_info['list'][i]['main']['temp']) - 273.15
    #fahrenheit = (celsius - 37) * (5/9) #placeholder in case I want to be able to switch to F
    temp_list.append(celsius)

  return temp_list


def check_pressure(weather_info, trigger):
  '''
  Function that checks the weather info and checks if a pressure trigger has been hit
  
  weather_info --> weather info from api
  trigger --> [above|below] [value]
  '''

  pressure_list = []
  for i in range(len((weather_info)['list'])):
    pressure_list.append(weather_info['list'][i]['main']['pressure'])

  return pressure_list


def check_humidity(weather_info, trigger):
  '''
  Function that checks the weather info and checks if a humidity trigger has been hit
  
  weather_info --> weather info from api
  trigger --> [above|below] [value]
  '''

  humidity_list = []
  for i in range(len((weather_info)['list'])):
    humidity_list.append(weather_info['list'][i]['main']['humidity'])

  return humidity_list


def check_wind(weather_info, trigger):
  '''
  Function that checks the weather info and checks if a wind trigger has been hit
  
  weather_info --> weather info from api
  trigger --> [above|below] [value]
  '''

  wind_list = []
  for i in range(len((weather_info)['list'])):
    wind_list.append(weather_info['list'][i]['wind']['speed'])

  return wind_list
