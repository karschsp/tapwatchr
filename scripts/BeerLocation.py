import simplejson as json

class BeerLocation(object):
  """ main class. Will be subclassed for each location """
  def __init__(self,name,url):
    self.name = name 
    self.url = url 
    self.data = None #list of beers
    self.resp = None

  def parse(self):
    """ set self.data to a python list: This function will be overridden with each implementation """
    n = self.name
    module = __import__(self.name)
    module.parse()
    print "parsed data "+self.name+" : "+self.url

  def cleaner(self):
    """ Clear function for general cleanup of raw data"""
    self.data = [beer.title() if beer.find('\'') ==-1 else beer for beer in self.data]
  
  def show_beers(self):
    """ Confirmation for parsed data """
    self.cleaner()
    print self.data

  def save_beers(self):
    """ Save the data to the json file """
    self.cleaner()
    s = json.dumps(self.data)
    f = open('../json/taps/' + self.name + '.json', 'w')
    f.write(s)
    f.close()

