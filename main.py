import os
import discord
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from fetch import fetch
from keep_alive import keep_alive
client = discord.Client()
cred = credentials.Certificate('flightline-vatsim-network-firebase-adminsdk-exzgg-ffa68b475c.json')
m = firebase_admin.initialize_app(cred, {'databaseURL': 'https://flightline-vatsim-network-default-rtdb.firebaseio.com/'})
ref = db.reference("/") 
channel_list = {
  'jtph-del': 951748103059410944,
  'jtph-gnd': 946276433519595560,
  'jtph-twr': 946276510170497115,
  'jtph-dep': 946276583054901259,
  'jtph-app': 946276583054901259,
  'jtph-ctr': 946276661060599848,
  'jxdx-del': 951748407335190538,
  'jxdx-gnd': 946277185893826560,
  'jxdx-twr': 946277277514215485,
  'jxdx-dep': 946277575855063070,
  'jxdx-app': 946277575855063070,
  'jxdx-ctr': 946277732680077363,
  'jsll-del': 951748484384559165,
  'jsll-gnd': 946277224473038889,
  'jsll-twr': 946277328177233950,
  'jsll-dep': 946277687654219826,
  'jsll-app': 946277687654219826,
  'jc04-twr': 946277396292710400,
  'uni': 946286014333333534 
} #Channel List

airList = {
  "DLH":"https://1000logos.net/wp-content/uploads/2017/03/Lufthansa-symbol.jpg",
  "ETD":"https://logosvector.net/wp-content/uploads/2015/08/etihad-airways-logo.png",
  "RYR":"https://w7.pngwing.com/pngs/502/989/png-transparent-flight-ryanair-bus-quick-click-fare-harp-blue-logo-transport.png",
  "SBS":"https://pbs.twimg.com/profile_images/793558336213962752/BggOIvca_400x400.jpg",
  "RXA":"https://media-exp1.licdn.com/dms/image/C560BAQES3DRLjWxhrg/company-logo_200_200/0/1635202894786?e=2147483647&v=beta&t=LjHG50MO-JhB094PQk3HWjqMy1JS2nfSV0fzgu4ZKsA",
  "NTJ":"https://worldairlinenews.files.wordpress.com/2018/05/netjet-logo.jpg?w=300&h=300",
  "LOG":"https://www.bricsaviation.com/wp-content/uploads/2020/02/0001_LOGANAIR-LOGO.jpg",
  "QXE":"https://www.baggagecircle.com/wp-content/uploads/2020/02/Alaska-Airlines-logo.jpg",
  "GAP":"https://pbs.twimg.com/profile_images/3380587485/bd6dbda93ba6bb500ebcc5f2bada74f5_400x400.jpeg",
  "BEE":"https://www.airline-suppliers.com/wp-content/uploads/2018/09/flybe-logo.png",
  "UAL":"https://pbs.twimg.com/profile_images/1410638840067506177/Uwza3ibI_400x400.jpg",
  "DJT":"https://media-exp1.licdn.com/dms/image/C4D0BAQFOntc4lbIoZg/company-logo_200_200/0/1616581604395?e=2159024400&v=beta&t=11uwCiDbL8G4sGM90_iZfh3p_Jqmav5SDsw-QPkcbgE",
  "AAL":"https://static.dezeen.com/uploads/2013/01/dezeen_American-Airlines-logo-and-livery_4a.jpg",
  "ICE":"https://seeklogo.com/images/I/Icelandair-logo-12D3F7F54F-seeklogo.com.png",
  "SWA":"https://yt3.ggpht.com/ZZwSBzlSCtokM14hjQTU7S_pJ2W8uUeLa0SU2q3NMZfo14nwTAGlTabCQ5UhCD44P6UCyJ69lWQ=s900-c-k-c0x00ffffff-no-rj",
  "SBI":"https://cdn.freelogovectors.net/wp-content/uploads/2020/01/s7-airlines-logo.png",
  "WJA":"https://fixwin10.com/wp-content/uploads/2021/07/WestJet-App-Review-Best-Apps-for-Windows-11.png",
  "GLO":"https://s3-symbol-logo.tradingview.com/gol-linhas-aereas-inteligentes--600.png",
  "WOW":"https://images.squarespace-cdn.com/content/v1/5ea2bcb7c4ac31691149f968/1587737408653-L0S5HCRAJUK6DJ14TJFC/wowair-logo-250x250.png",
  "SAS":"https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/v1491203029/vikrvcwojbngkainiwja.png",
  "THY":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStVEwy81594f6UVjA0KurGDL5CZGNe8O5N7g&usqp=CAU",
  "CPA":"https://s3-symbol-logo.tradingview.com/cathay-pacific--600.png",
  "KLM":"https://i.pinimg.com/736x/2a/50/0e/2a500e7d351a5cbb89294dd93628d9b4--logo-service-hotel-logo.jpg",
  "VIR":"https://i.pinimg.com/originals/0a/2a/12/0a2a12a6df3b43adc555a9e2768bd577.jpg",
  "QFA":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1QCFh3AYTcIX330APssdzJ2Bf0TB5JlYJsW5fdhucQ6SWuePgzgOrrOyI5sSTLurNVMY&usqp=CAU",
  "THA":"https://awards.brandingforum.org/wp-content/uploads/2019/11/Thai-Airways-Portfolio-logo-01-1024x1024.jpg",
  "JAL":"https://s3-symbol-logo.tradingview.com/japan-airlines--600.png",
  "TOM":"https://w7.pngwing.com/pngs/692/931/png-transparent-tui-group-tui-uk-hotel-tui-travel-hotel-text-smiley-emoticon.png",
  "ETH":"https://cdn.freebiesupply.com/logos/large/2x/ethiopian-airlines-logo-png-transparent.png"
} #Logo List

@client.event
async def on_ready():
  print(f"{client.user} is online...")
@client.event
async def on_message(message):
  if message.content.startswith("!initfp"):
    global fp
    guild = client.get_guild(945845395609776148)
    fp = fetch(message.content)
    name = message.author.nick
    img = airList[fp[0][0:3]]
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
      await client.get_channel(channel_list['jtph-del']).send(embed=embed)
    if fp[1] == "JSLL":
      await client.get_channel(channel_list['jsll-del']).send(embed=embed)
    if fp[1] == "JXDX":
      await client.get_channel(channel_list['jxdx-del']).send(embed=embed)
    if fp[1] == "JC04":
      await client.get_channel(channel_list['jtph-del']).send(embed=embed)
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
