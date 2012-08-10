#! /usr/bin/env python
import urllib2 as l2
import lxml.html
import smtplib
from lxml.cssselect import CSSSelector
from email.mime.text import MIMEText

def sendme(mailtext):
  msg = MIMEText(mailtext)
  msg['Subject'] = 'Victory - OnTap'
  me = 'steve@stevekarsch.com'
  you = 'steve@stevekarsch.com'
  msg['From'] = me
  msg['To'] = you
  s = smtplib.SMTP('localhost')
  s.sendmail(me,[you],msg.ad_string())
  s.quit()

tappath='//div[@class="content"]/table/tbody/tr[2]/td[1]'
resp = l2.urlopen('http://victorybeer.com/brewpub/on-tap')
data = resp.read()
doc = lxml.html.fromstring(data)
resraw = doc.xpath(tappath)
rawbeers = [x.text_content() for x in resraw]
beers = rawbeers[0].split('\n')
beers_str = '\n'.join(beers)
simplebeers = beers_str.encode('ascii', 'ignore')
sendme(simplebeers)
