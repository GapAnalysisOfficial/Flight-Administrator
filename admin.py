import os
import discord
from fetch import fetch
client = discord.Client()

@client.event
async def on_ready():
  print(f"{client.user} Online...")

@client.event
async def on_message(message):
  if message.content.startswith("!ping"):
    late = client.latency * 1000
    await message.channel.send(f"Ping: {late} ms.")
  if message.content.startswith('!initmem'):
    data = fetch(message.content)
    if data[0].lower() == 'atc' or data[0].lower() == 'p':
      pass
    else:
      await message.channel.send(f"Your input '{data[0]}' is not recognized by the Admin. Please Try Again...")
my_secret = os.environ['TOKEN']
client.run(my_secret)
