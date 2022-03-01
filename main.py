import os
import discord
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from fetch import fetch
client = discord.Client()
cred = credentials.Certificate('flightline-vatsim-network-firebase-adminsdk-exzgg-ffa68b475c.json')
m = firebase_admin.initialize_app(cred, {'databaseURL': 'https://flightline-vatsim-network-default-rtdb.firebaseio.com/'})
ref = db.reference("/") 
channel_list = {
  'jtph-del': 946210173695975427,
  'jtph-gnd': 946276433519595560,
  'jtph-twr': 946276510170497115,
  'jtph-dep': 946276583054901259,
  'jtph-app': 946276583054901259,
  'jtph-ctr': 946276661060599848,
  'jxdx-del': 946277088636338207,
  'jxdx-gnd': 946277185893826560,
  'jxdx-twr': 946277277514215485,
  'jxdx-dep': 946277575855063070,
  'jxdx-app': 946277575855063070,
  'jxdx-ctr': 946277732680077363,
  'jsll-del': 946277126573817866,
  'jsll-gnd': 946277224473038889,
  'jsll-twr': 946277328177233950,
  'jsll-dep': 946277687654219826,
  'jsll-app': 946277687654219826,
  'jc04-twr': 946277396292710400,
  'uni': 946286014333333534 
}
@client.event
async def on_ready():
  print(f"{client.user} is online...")
@client.event
async def on_message(message):
  fl = db.reference(f'/flights/{message.author.id}')
  if message.content.startswith("!initfp"):
    global fp
    fp = fetch(message.content)
    fl.push({fp[0]: {'Source': fp[1], 'Destination': fp[2], 'Departure Gate': fp[3], 'Equipment': fp[4], 'Route': fp[5], 'Flight Rules': fp[6], 'Cruising Altitude': fp[7], 'Cruising Speed': fp[8], 'Squawk Code': '','Departure Runway': '', 'Departure Taxi Path': '', 'Climb level': '', 'ILS Clearance': '', 'Approach Runway': '', 'Arrival Taxi Path': '', 'Arrival Gate': '', 'Clearance': '', 'DEP Ground Connect': '', 'DEP TWR Connect': '', 'DEP Connect': '', 'DEP Centre Connect': '', 'ARR Centre Connect': '', 'ARR Connect': '', 'DEP TWR Connect': '', 'DEP Ground Connect': ''}})
    struct = f">>> Flight Number: {fp[0]}\nSource: {fp[1]}\nDestination: {fp[2]}\nGate: {fp[3]}\nEquipment: {fp[4]}\nRoute: {fp[5]}\nFlight Rules: {fp[6]}\nCruising Altitude: {fp[7]}\nCrusing Speed: {fp[8]}\nStatus: Flight Plan Filed. Requesting {fp[6]} clearance to {fp[2]}."
    if fp[1] == 'JTPH':
      await client.get_channel(channel_list['jtph-del']).send(struct)
    if fp[1] == "JSLL":
      await client.get_channel(channel_list['jsll-del']).send(struct)
    if fp[1] == "JXDX":
      await client.get_channel(channel_list['jxdx-del']).send(struct)
    if fp[1] == "JC04":
      await client.get_channel(channel_list['jtph-del']).send(struct)
  if message.content.startswith("!clear"):
    n = fl.get()
    status = False
    for i in n:
      if i == fp[0]:
        status = True
    if status:
      pass
    else:
      await message.channel.send(f"No Flight Plan Filed as {fp[0]}")

      
my_secret = os.environ['TOKEN']
client.run(my_secret)
