import jinja2
import os
import webapp2
import logging   # console loglib
import json

from google.appengine.api import urlfetch  # request  lib
from model.room import Room
from model.type import Type 
from model.device import Device 


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/home/view')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) 

class Main_Settings(webapp2.RequestHandler):

    roomcheck = False
    typecheck = False

    def get(self):
        templatevalues = {
            'roomcheck' : Main_Settings.roomcheck,
            'typecheck' : Main_Settings.typecheck,
        }
        template = jinja_environment.get_template('set_main.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))
        if (Main_Settings.roomcheck == True):
            Main_Settings.roomcheck = False
        if (Main_Settings.typecheck == True):
            Main_Settings.typecheck = False

    def post(self):
        if (self.request.get('roomname') == ''):
            typedevice = Type(devicetype = self.request.get('devicetype'))
            typedevice.put()
            Main_Settings.typecheck = True
        else:
            room = Room(roomname = self.request.get('roomname'))
            room.put()
            Main_Settings.roomcheck = True
        return webapp2.redirect('/settings')

class Device_Settings(webapp2.RequestHandler):
    check = False
    def get(self):
        devicetype = Type.query()
        room = Room.query()
        templatevalues = {
            'rooms' : room,
            'devicetypes' : devicetype,
            'pin' : 16,
            'check' : Device_Settings.check,
        }
        if (Device_Settings.check == True):
            Device_Settings.check = False 
        template = jinja_environment.get_template('set_device.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))
    
    def post(self):
        device = Device(pin = int(self.request.get('pin')),
            devicetype = self.request.get('devicetype'),
            roomname = self.request.get('room'))
        device.put()
        Device_Settings.check = True
        return webapp2.redirect('/add-device')

    #def post(self):
	#	url = "https://api.github.com/"
	#	res = urlfetch.fetch(url)
	#	if res.status_code == 200:
	#		mom = "ssdsd"
	#		top = "44434"
	#		lol = mom + top + '\n'
	#		for i in range(5):
	#			self.response.write(lol)
	#		#logging.info(res.content)
	#		j = json.loads(res.content)
  	#		self.response.write(j['starred_url'])