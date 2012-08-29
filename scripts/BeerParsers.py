import urllib2 as l2
import lxml.html


def Victory(clas):
    tappath='//div[@class="content"]/table/tbody/tr[2]/td[1]'
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
    cleaned = [z.lstrip('* ') for z in rawbeers[0] if isinstance(z,str) and z.startswith("*")]
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
