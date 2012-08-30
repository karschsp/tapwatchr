import simplejson as json
from BeerLocation import BeerLocation
import BeerParsers

with open('../json/taps.json', 'r') as f:
  taps = json.loads(f.read())

  for tap in taps["Taps"]:
    loc = BeerLocation(tap["ShortName"], tap["URL"])
    if loc.name.startswith('IronHill'):
      getattr(BeerParsers,'IronHill')(loc)
    else:
      getattr(BeerParsers,loc.name)(loc)

    loc.show_beers()
    loc.save_beers()
