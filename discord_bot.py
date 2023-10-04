#matthew tamer
#libraries
import discord
import os
import random
import requests  #for working with apis
import json  #apis return json files
from weather_info import get_weather_info, get_weather
from replit import db  #database
#from keep_alive import keep_alive

encouragement_list = []

token = os.environ['DISCORD_TOKEN']
client = discord.Client(intents=discord.Intents.all())


#called when bot is ready to be used
@client.event
async def on_ready():
  #print to console that it is online with the username
  print('We have logged in as {0.user}'.format(client))


# called when bot senses a message
@client.event
async def on_message(message):
  #dont do anything if the message is from the bot itself
  if message.author == client.user:
    return
  msg = message.content  
  if msg.startswith('$commands'):
    await message.channel.send("$commands --> Sends this Message \n" 
                               "$setlocation [city] [country code] --> Sets the location to check the weather. Country code is the 2 letters that describe your country. Example Canada = CA \n" 
                               "$location --> Checks what the location is currently set to. \n"
                               "$weather [now|today|week] --> Sends the current forecast \n"
                               "$setalert [alert] --> Creates a certain weater alert to notify the user about")
  
  #allow user to set their location
  if msg.startswith('$setlocation '):
    location = msg.split()[1]
    country = msg.split()[2]
    locationstring = get_weather_info(location, country)[1] #write to database
    countrystring = get_weather_info(location, country)[2] #write to database
    await message.channel.send(f"Setting {locationstring}, {countrystring} as your location. ")
    
  if msg.startswith('$location'):
    pass
  if msg.startswith('$weather '):
    timeframe = msg.split[1]
    location = 1 #get from database
    if get_weather(location, timeframe) != 'error':
      pass
    else:
      await message.channel.send("Invalid timeframe. Command usage: $weather [now|today|week[")
  if msg.startswith('$setalert '):
    pass

#keep_alive() implement later, have it also check the full weather for alerts every time it is pinged if possible
client.run(token)
