import urllib2 as l2
import lxml.html
import html2text
from bs4 import BeautifulSoup
import types

def StationTaproom(clas):

    #tappath = '//tbody[@class="taplist"]'
    resp = l2.urlopen(clas.url)
    data = resp.read()
    soup = BeautifulSoup(data)
    taplist = soup.find("tbody", class_='taplist')
    for item in taplist:
      print item
    #taplist = '<tbody class="taplist"><tr><td><div style="text-align: center;"><span style="color: #c0c0c0;"><span style="text-decoration: underline;">Tap List</span></span></div><div style="text-align: center;"><span style="color: #c0c0c0;"><span style="text-decoration: underline;"><br/></span></span></div><div style="text-align: center;"><span style="color: #c0c0c0;">Allagash White</span></div><div style="text-align: center;"><span style="color: #c0c0c0;">Sierra Nevada Tumbler</span></div><div style="text-align: center;"><span style="color: #c0c0c0;">Lefthand Sawtooth Nitro</span></div><div style="text-align: center;"><span style="color: #c0c0c0;">Sly Fox Grisette</span></div><div style="text-align: center;"><span style="color: #c0c0c0;">Grassroots Kolving Bryggerloug</span></div><div style="text-align: center;"><span style="color: #c0c0c0;">Sierra Nevada Torpedo</span></div></td><td style="text-align: center;"><span style="text-decoration: underline;"><span style="color: #c0c0c0;">Updated 8.28.12</span></span><p><span style="color: #c0c0c0;">Anchor Liberty Ale<br/></span>Lagunitas Lil Sumpin Wild<br/>Green Flash Imperial IPA<br/>Ayinger Brauweiss<br/><span style="color: #c0c0c0;">Rogue Brutal Bitter<br/></span>Sly Fox Pikeland Pils</p><p><span style="color: #c0c0c0;">CASK: Victory Headwaters</span></p></td></tr></tbody>'
    #print html2text.html2text(taplist)
    # doc = lxml.html.fromstring(data)
    # resraw = doc.xpath(tappath)
    #rawbeers = [x.text_content().split('\n') for x in resraw]
    #for rawbeer in rawbeers:
    #  for beer in rawbeer:
    #    print 'BEER' + beer + '\n'
    #clas.data = rawbeers
