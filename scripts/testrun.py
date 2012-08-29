import sys
import simplejson as json
from BeerLocation import BeerLocation
import BeerParsers

locationtotest = sys.argv[1]

f = open('../json/taps.json', 'r')
taps = json.loads(f.read())

for tap in taps["Taps"]:
  if tap["ShortName"] == locationtotest:
    loc = BeerLocation(tap["ShortName"], tap["URL"])
    print "Checking " + tap["URL"] + "\n"
    getattr(BeerParsers,loc.name)(loc)
    loc.show_beers()
    #loc.save_beers()
