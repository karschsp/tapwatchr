import simplejson as json
from BeerLocation import BeerLocation
import BeerParsers
import datetime
import os,sys

dir = sys.path[0]
with open(dir + '/../json/taps.json', 'r') as f:

  taps = json.loads(f.read())

  for tap in taps["Taps"]:
    loc = BeerLocation(tap["ShortName"], tap["URL"])
    if loc.name.startswith('IronHill'):
      getattr(BeerParsers,'IronHill')(loc)
    else:
      getattr(BeerParsers,loc.name)(loc)

    loc.show_beers()
    loc.save_beers()

f = open(dir + '/../json/lastrun.txt', 'w')
f.write(str(datetime.datetime.now()))
f.close()
