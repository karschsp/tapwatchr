#! /usr/bin/env python

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import sqlite3
import json

app = Flask(__name__)
app.config.from_envvar('TW_SETTINGS', silent=True)

@app.route('/')
def show_home():
  #return render_template('template_home.htm')
  return '<html><body><a href="locations">locations</a></body></html>'

@app.route('/locations')
def show_locations():
  with open('../json/taps.json','r') as f:
    taps = json.loads(f.read())
    #return taps
    t = [(tap['ShortName'],tap['URL']) for tap in taps['Taps']]
    r = ''
    for tap in taps['Taps']:
      r +='<br/>'+tap['ShortName']
    return r
   
  #return render_template('template_locations.htm')



if __name__ =='__main__':
 app.debug = True
 app.run(host='0.0.0.0') 
