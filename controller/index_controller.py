import jinja2
import os
import webapp2
import MySQLdb
import logging   # console loglib
import json
from time import gmtime, strftime
from controller.device_helper import deviceHelper



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/home/view')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) 

class Main(webapp2.RequestHandler):

    def get(self):
        db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM History')
        history = cursor.fetchall()
        db.close()
    	templatevalues = {
            'history' : history,
            'time' : strftime("%X", gmtime()),
            'year' : strftime(" %d %b %Y ", gmtime()),
            'temperature' : 40,#deviceHelper.checkHumTemp(deviceHelper,"temperature"),
            'humidity' : 20,#deviceHelper.checkHumTemp(deviceHelper,"humidity"),
        }
        template = jinja_environment.get_template('weather.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))


