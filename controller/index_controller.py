import jinja2
import os
import webapp2
import logging   # console loglib
import json

from google.appengine.api import urlfetch  # request  lib
from google.appengine.ext import ndb
from model.room import Room
from model.device import Device  


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/home/view')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) 

class Main(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('room_plan.html')
        self.response.out.write(template.render())

class Light(webapp2.RequestHandler):

    def get(self):
    	lightdevice = Device.query(Device.devicetype == 'light').order(Device.roomname)
    	room = Room.query().order(Room.roomname)
    	rooms = []
    	for a in room:
    		for b in lightdevice:
    			if (a.roomname == b.roomname): 
    				rooms.append(a.roomname)
    	rooms = set(rooms)
    	templatevalues = {
            'rooms' : rooms,
            'lightdevices' : lightdevice,
        }
        template = jinja_environment.get_template('light.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))

class Climate(webapp2.RequestHandler):

    def get(self):
    	climatedevice = Device.query(ndb.OR(Device.devicetype == 'warm floor',Device.devicetype == 'heating',Device.devicetype == 'air conditioner')).order(Device.roomname).order(Device.devicetype)
    	room = Room.query().order(Room.roomname)
    	rooms = []
    	for a in room:
    		for b in climatedevice:
       			if (a.roomname == b.roomname): 
    				rooms.append(a.roomname)
    	rooms = set(rooms)
    	templatevalues = {
            'rooms' : rooms,
            'climatedevices' : climatedevice,
        }
        template = jinja_environment.get_template('climate.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))

