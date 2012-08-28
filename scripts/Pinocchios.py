#! /usr/bin/env python

import urllib2 as l2
import lxml.html

from BeerLocation import BeerLocation

class Pinocchios(BeerLocation):

  def parse(self):
    tappath='//div[@id="mid"]/article/div/strong'
    resp = l2.urlopen(self.url)
    data = resp.read()
    doc = lxml.html.fromstring(data)
    resraw = doc.xpath(tappath)
    rawbeers = [x.text_content() for x in resraw]
    self.data = rawbeers 

