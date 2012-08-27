
class BeerLocation(object):
  """ main class. Will be subclassed for each location """
  def __init__(self,name,url):
    self.name = name 
    self.url = url 
    self.data = None #list of beers
    self.resp = None

  def parse(self):
    """ set self.data to a python list: This function will be overridden with each implementation """
    print "parsed data "+self.name+" : "+self.url
  
  def show_beers(self):
    """ Confirmation for parsed data """
    print self.data

  def save_beers(self):
    """ Save the data to the sqlite DB """

    
 