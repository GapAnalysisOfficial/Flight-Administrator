import os
import discord
import firebase_admin
from firebase_admin import credentials
#from firebase_admin import db
client = discord.Client()
cred = credentials.Certificate()
m = firebase_admin.initialize_app(config)
fp = []
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
def initFlightPlan(command):
  store = []
  data = command
  data = data + "-"
  start = 0
  stop = 0
  temp = ""
  while stop < len(data):
      if data[stop] != "-":
          stop += 1
      else:
          temp = data[start:stop]
          store.append(temp)
          start = stop + 1
          stop += 1

  store.pop(0)
  return store
@client.event
async def on_ready():
  print(f"{client.user} is online...")

@client.event
async def on_message(message):
  if message.content.startswith("!initfp"):
    fp = initFlightPlan(message.content)
    struct = f">>> Flight Number: {fp[0]}\nSource: {fp[1]}\nDestination: {fp[2]}\nGate: {fp[3]}\nEquipment: {fp[4]}\nRoute: {fp[5]}\nFlight Rules: {fp[6]}\nCruising Altitude: {fp[7]}\nCrusing Speed: {fp[8]}\nStatus: Flight Plan Filed."
    if fp[1] == 'JTPH':
      await client.get_channel(channel_list['jtph-del']).send(struct)
    if fp[1] == "JSLL":
      await client.get_channel(channel_list['jsll-del']).send(struct)
    if fp[1] == "JXDX":
      await client.get_channel(channel_list['jxdx-del']).send(struct)
    if fp[1] == "JC04":
      await client.get_channel(channel_list['jtph-del']).send(struct)
      
my_secret = os.environ['TOKEN']
client.run(my_secret)
