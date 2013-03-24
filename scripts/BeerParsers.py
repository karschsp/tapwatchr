import urllib2 as l2
from lxml.html import tostring, html5parser
import lxml.html
import html2text

def Victory(clas):
    tappath="//h3[text()='On Draft']/following-sibling::div[contains(@class,'twocol-one')]//a";
    resp = l2.urlopen(clas.url)
    data = resp.read()
    doc = lxml.html.fromstring(data)
    resraw = doc.xpath(tappath)
    rawbeers = [x.text_content() for x in resraw]
    beers = rawbeers[0].split('\n')
    #beers_str = '\n'.join(beers)
    #simplebeers = beers_str.encode('ascii','ignore')
    cleaned = [beer for beer in beers if not beer.isspace()]
    clas.data = cleaned 


def Pinocchios(clas):
    tappath='//div[@id="mid"]/article/div/strong'
    resp = l2.urlopen(clas.url)
    data = resp.read()
    doc = lxml.html.fromstring(data)
    resraw = doc.xpath(tappath)
    rawbeers = [x.text_content() for x in resraw]
    clas.data = rawbeers 

def DraftingRoom(clas):
    tappath='//div[@class="post-body entry-content"]'
    resp = l2.urlopen(clas.url)
    data = resp.read()
    doc = lxml.html.fromstring(data)
    resraw = doc.xpath(tappath)
    rawbeers = [x.text_content().split('\n') for x in resraw]
    #print rawbeers
    cleaned = [z.lstrip('* ') for z in rawbeers[0] if z]
    #print cleaned
    clas.data = cleaned

def IronHill(clas):
    tappath = '//h4[@class="monthly"]'
    resp = l2.urlopen(clas.url)
    data = resp.read()
    doc = lxml.html.fromstring(data)
    resraw = doc.xpath(tappath)
    rawbeers = [x.text_content() for x in resraw]
    #beers_str = '\n'.join(rawbeers)
    #simplebeers = beers_str.encode('ascii', 'ignore')
    clas.data = rawbeers

def GreatAmericanPubWayne(clas):
    tappath = '//div[@class="menuItemTitle"]'
    resp = l2.urlopen(clas.url)
    data = resp.read()
    doc = lxml.html.fromstring(data)
    resraw = doc.xpath(tappath)
    rawbeers = [x.text_content() for x in resraw]
    beers = [beer.strip() for beer in rawbeers]
    clas.data = beers

def CoccosAston(clas):
    tappath = '//span[@class="menu_item"]'
    resp = l2.urlopen(clas.url)
    data = resp.read()
    doc = lxml.html.fromstring(data)
    resraw = doc.xpath(tappath)
    rawbeers = [x.text_content() for x in resraw]
    clas.data = rawbeers

def ThreeTides(clas):
  resp = l2.urlopen(clas.url)
  data = resp.read()
  tappath = '//html/body/table/tr[2]/td/table/tr/td/table/tr[2]/td/table/tr[2]/td[2]'
  doc = lxml.html.fromstring(data)
  raw = doc.xpath(tappath)
  for x in raw:
    rawbeers = html2text.html2text(tostring(x))

  beers = rawbeers.split('\n')
  cleaned = [beer for beer in beers if not beer.isspace() and beer.find('*') == -1]
  clas.data = cleaned

def SlyFoxPhoenixville(clas):
  resp = l2.urlopen(clas.url)
  data = resp.read()
  tappath = '/html/body/div/table/tr/td/table/tr[3]/td[1]/div//a'
  doc = lxml.html.fromstring(data)
  rawbeers = doc.xpath(tappath)
  beers = [beer.text_content() for beer in rawbeers]
  clas.data = beers

def SlyFoxPottstown(clas):
  resp = l2.urlopen(clas.url)
  data = resp.read()
  tappath = '/html/body/div/table/tr/td/table/tr[3]/td[2]//a'
  doc = lxml.html.fromstring(data)
  rawbeers = doc.xpath(tappath)
  beers = [beer.text_content() for beer in rawbeers]
  clas.data = beers

def Dogfish(clas):
  resp = l2.urlopen(clas.url)
  data = resp.read()
  tappath = '/html/body/div[2]/div[3]/div[3]/div/div/div[3]/div//p'
  doc = lxml.html.fromstring(data)
  rawbeers = doc.xpath(tappath)
  beers = [beer.text_content() for beer in rawbeers]
  cleaned = [beer for beer in beers if not beer.isspace() and beer.find('%') > 0]
  clas.data = cleaned

def CraftAleHouse(clas):
  resp = l2.urlopen(clas.url)
  data = resp.read()
  tappath = '//div[@id="sidebar-left-1"]/div[@id="TextList1"]//li'
  doc = lxml.html.fromstring(data)
  rawbeers = doc.xpath(tappath)
  beers = [x.text_content() for x in rawbeers]
  clas.data = beers

def WestBradfordGrill(clas):
  resp = l2.urlopen(clas.url)
  data = resp.read()
  #tappath = '//div[@id="sidebar-left-1"]/div[@id="TextList1"]//li'
  #doc = lxml.html.fromstring(data)
  a = lxml.html.fromstring(data)
  print tostring(a)

  #rawbeers = doc.xpath(tappath)
  #beers = [x.text_content() for x in rawbeers]
  #clas.data = beers


def Rollies(clas):
  resp = l2.urlopen(clas.url)
  data = resp.read()
  tappath = '/html/body/table/tr/td/table/tr[4]/td/table/tr/td/table/tr/td/table/tr/td/table/tr[4]/td/table/tr//td'
  doc = lxml.html.fromstring(data)
  rawbeers = doc.xpath(tappath)
  beers = list()
  tmpbeers = list()
  for x in rawbeers:
    tmpbeers = x.text_content().split('\n')
    for beer in tmpbeers:
      beers.append(beer)

  clas.data = beer
