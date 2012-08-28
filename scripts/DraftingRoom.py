#! /usr/bin/env python

import urllib2 as l2
import lxml.html

from BeerLocation import BeerLocation

class DraftingRoom(BeerLocation):

  def parse(self):
    tappath='//div[@class="post-body entry-content"]'
    resp = l2.urlopen(self.url)
    data = resp.read()
    doc = lxml.html.fromstring(data)
    resraw = doc.xpath(tappath)
    rawbeers = [x.text_content().split('\n') for x in resraw]
    #print rawbeers
    cleaned = [z.lstrip('* ') for z in rawbeers[0] if isinstance(z,str) and z.startswith("*")]
    #print cleaned
    self.data = cleaned 

