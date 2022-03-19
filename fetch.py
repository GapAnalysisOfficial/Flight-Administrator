from datetime import date
def fetch(command): #fetch individual elements from a string into an array
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

def channel_list(channel): #fetch channels from the channels dictionary
  channels = {
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
  }
  return channels[channel]

def icon_search(company):
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
  }
  return airList[company]

def flight_plan(**data):
  year = "%Y"
  month = "%B"
  day = "%d"
  fp = {year:{
    month:{
      day:{
        data[callsign]:{
          "flight-rules": data[fr],
          "type-of-aircraft": data[toa],
          "wake-turbulence-category": data[wtc],
          "departure-aerodrome": data[dpa],
          "cruising-speed": data[cs],
          "cruising-altitude": data[ca],
          "route": data[r],
          "destination aerodrome": data[dna],
          "alternate-aerodrome": data[aa],
          "supplmentary-information": data[si],
          "squawk-code": data[sc],
          "departure-gate": data[dg],
          "departure-runway": data[dr],
          "departure-delivery-clearance": data[ddc],
          "departure-taxi-route": data[dtr],
          "departure-ground-clearance": data[dgc],
          "departure-tower-clearance": data[dtc],
          "departure-departure-clearance": data[ddpc],
          ""
        }
      }
    }
  }}

  return fp