# -*- coding: utf-8 -*- 
import jinja2
import os
import webapp2
import MySQLdb
import logging   # console loglib
import json


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/home/view')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) 


class Light(webapp2.RequestHandler):

    def get(self):
    	db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
        cursor = db.cursor()
        cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "light"')
    	lightdevice = cursor.fetchall()
    	cursor.execute('SELECT roomname FROM Room')
    	room = cursor.fetchall()
    	rooms = []
    	for a in room:
    		for b in lightdevice:
    			if (a[0] == b[2]): 
    				rooms.append(a[0])
    	rooms = set(rooms)
    	templatevalues = {
            'rooms' : rooms,
            'lightdevices' : lightdevice,
        }
        db.close()
        template = jinja_environment.get_template('light.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))