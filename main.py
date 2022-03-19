import os
import discord
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from fetch import fetch, channel_list, icon_search
from keep_alive import keep_alive
client = discord.Client()
cred = credentials.Certificate('flightline-vatsim-network-firebase-adminsdk-exzgg-ffa68b475c.json')
m = firebase_admin.initialize_app(cred, {'databaseURL': 'https://flightline-vatsim-network-default-rtdb.firebaseio.com/'})
ref = db.reference("/") 

@client.event
async def on_ready():
  print(f"{client.user} is online...")
@client.event
async def on_message(message):
  if message.content.startswith("!initfp"):
    global fp
    guild = client.get_guild(945845395609776148)
    fp = fetch(message.content)
    name = message.author.display_name
    img = icon_search(fp[0][0:3])
    embed = discord.Embed(title=str(f"***{fp[0]} FLIGHT PLAN***"), colour=0xF0A500, description=str(f"{name} created a flight plan from {fp[1]} to {fp[2]}"))
    embed.set_thumbnail(url=img)
    embed.set_author(name=name, icon_url=f"{message.author.avatar_url}")
    embed.set_footer(text=guild, icon_url=guild.icon_url)
    embed.add_field(name="Flight No.", value=fp[0])
    embed.add_field(name="Source", value=fp[1])
    embed.add_field(name="Destination", value=fp[2])
    embed.add_field(name="Gate", value=fp[3])
    embed.add_field(name="Equipment", value=fp[4])
    embed.add_field(name="Route", value=fp[5])
    embed.add_field(name="Flight Rules", value=fp[6])
    embed.add_field(name="Cruising Altitude", value=fp[7])
    embed.add_field(name="Cruising Speed", value=fp[8])
    embed.add_field(name="Status", value="Ready for delivery clearance")
    ref = db.reference("flights")
    data = ref.get()
    l = []
    for i in data.keys():
      l.append(i)

    name = fp[0]
    for j in l:
      if j == name:
        await message.channel.send(f"{fp[0]} Flight Plan has already filed by someone. Requesting to change your callsign. Thank You.")
      else:
        dum = {f'{fp[0]}':{'aGate': '','aRwy': '','aTaxiroute': '',
            'aaClearance': 0,
            'acClearance': 0,
            'agClearance': 0,
            'atClearance': 0,
            'crusingAlt': f'{fp[7]}',
            'crusingSpd': f'{fp[8]}',
            'dClimb': '',
            'dRwy': '',
            'dcClearance': 0,
            'ddClearance': 0,
            'ddpClearance': 0,
            'destination': f'{fp[2]}',
            'dgClearance': 0,
            'dtClearance': 0,
            'eqp': f'{fp[4]}',
            'flightRules': f'{fp[6]}',
            'gate': f'{fp[3]}',
            'route': f'{fp[5]}',
            'source': f'{fp[1]}',
            'sq': '',
            'taxiRoute': ''
          }
        }
        data.update(dum)
        ref.set(data)
    if fp[1] == 'JTPH':
      await client.get_channel(channel_list('jtph-del')).send(embed=embed)
    if fp[1] == "JSLL":
      await client.get_channel(channel_list('jsll-del')).send(embed=embed)
    if fp[1] == "JXDX":
      await client.get_channel(channel_list('jxdx-del')).send(embed=embed)
    if fp[1] == "JC04":
      await client.get_channel(channel_list('jtph-del')).send(embed=embed)
  if message.content.startswith("!clear"):
    n = []
    status = False
    for i in n:
      if i == fp[0]:
        status = True
    if status:
      pass
    else:
      await message.channel.send(f"No Flight Plan Filed as {fp[0]}")

      
my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)
