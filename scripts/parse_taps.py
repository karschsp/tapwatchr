import simplejson as json
from BeerLocation import BeerLocation

f = open('../json/taps.json', 'r')
taps = json.loads(f.read())

for tap in taps["Taps"]:
  # print 'here...'
  # print tap["URL"]
  loc = BeerLocation(tap["ShortName"], tap["URL"])
  loc.parse()
  loc.show_beers()

