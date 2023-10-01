#matthew tamer
#libraries
import discord
import os
import random
import requests #for working with apis
import json #apis return json files
import weather_info
from replit import db #database
from keep_alive import keep_alive


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


#keep_alive() implement later
client.run(token)
