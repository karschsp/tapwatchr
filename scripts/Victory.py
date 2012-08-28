#! /usr/bin/env python

import urllib2 as l2
import lxml.html

from BeerLocation import BeerLocation

class Victory(BeerLocation):

  def parse(self):
    tappath='//div[@class="content"]/table/tbody/tr[2]/td[1]'
    resp = l2.urlopen(self.url)
    data = resp.read()
    doc = lxml.html.fromstring(data)
    resraw = doc.xpath(tappath)
    rawbeers = [x.text_content() for x in resraw]
    beers = rawbeers[0].split('\n')
    #beers_str = '\n'.join(beers)
    #simplebeers = beers_str.encode('ascii','ignore')
    cleaned = [beer for beer in beers if not beer.isspace()]
    self.data = cleaned 

