import jinja2
import os
import webapp2
import MySQLdb
import logging   # console loglib
import json
import urllib2
from controller.device_helper import deviceHelper

from google.appengine.api import urlfetch  # request  lib



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/home/view')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Main_Settings(webapp2.RequestHandler):

    roomcheck = False
    typecheck = False
    check = False
    def get(self):
        db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
        cursor = db.cursor()
        cursor.execute('SELECT devicetype FROM Type')
        devicetype = cursor.fetchall()
        cursor.execute('SELECT roomname FROM Room')
        room = cursor.fetchall()
        templatevalues = {
            'rooms' : room,
            'devicetypes' : devicetype,
            'pin' : 16,
            'check' : Main_Settings.check,
            'roomcheck' : Main_Settings.roomcheck,
            'typecheck' : Main_Settings.typecheck,
        }
        db.close()        
        template = jinja_environment.get_template('set_main.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))
        if (Main_Settings.check == True):
            Main_Settings.check = False 
        if (Main_Settings.roomcheck == True):
            Main_Settings.roomcheck = False
        if (Main_Settings.typecheck == True):
            Main_Settings.typecheck = False

    def post(self):
        db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
        cursor = db.cursor()
        if (self.request.get('roomname') == '' and self.request.get('devicetype') ==''):
            cursor.execute('INSERT INTO Device (pin,devicetype,roomname) VALUES (%s,%s,%s)',(self.request.get('pin'),self.request.get('type'),self.request.get('room')))
            typ = "i"
            if (self.request.get('type') == "move" or self.request.get('devicetype') == "reed" or self.request.get('devicetype') == "humidity" or self.request.get('devicetype') == "temperature"):
                typ = "i"
            else:
                typ = "o"
            deviceHelper.setMode(deviceHelper,self.request.get('pin'),typ)    
            if (typ == "o"):
                deviceHelper.ternOff(deviceHelper,self.request.get('pin'))
            Main_Settings.check = True    
        elif (self.request.get('roomname') == '' and self.request.get('devicetype') !=''):
            cursor.execute('INSERT INTO Type (devicetype) VALUES (%s)', (self.request.get('devicetype')))
            Main_Settings.typecheck = True
        elif(self.request.get('roomname') != '' and self.request.get('devicetype') ==''):
            cursor.execute('INSERT INTO Room (roomname) VALUES (%s)', (self.request.get('roomname')))
            Main_Settings.roomcheck = True
        db.commit()
        db.close()
        return webapp2.redirect('/settings')

class Delete_Device(webapp2.RequestHandler):
    check = False
    def get(self):
        db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Device ORDER BY roomname, pin')
        devices = cursor.fetchall()
        cursor.execute('SELECT * FROM Room ORDER BY roomname')
        rooms = cursor.fetchall()
        cursor.execute('SELECT * FROM Type ORDER BY devicetype')
        types = cursor.fetchall()
        templatevalues = {
            'devices' : devices,
            'types' : types,
            'rooms' : rooms,
            'check': Delete_Device.check,
        }        
        db.close()
        template = jinja_environment.get_template('delete_device.html')
        self.response.out.write(template.render({'templatevalues':templatevalues}))
    
        

class Delete(webapp2.RequestHandler):
    
    def get(self,id):
        db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
        cursor = db.cursor()
        cursor.execute('DELETE FROM Device WHERE id = %s',int(id))
        db.commit()
        db.close()
        Delete_Device.check = True
        return webapp2.redirect('/delete-device')

class Delete1(webapp2.RequestHandler):
    
    def get(self,id):
        db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
        cursor = db.cursor()
        cursor.execute('DELETE FROM Type WHERE id = %s',int(id))
        db.commit()
        db.close()
        Delete_Device.check = True
        return webapp2.redirect('/delete-device')

class Delete2(webapp2.RequestHandler):
    
    def get(self,id):
        db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
        cursor = db.cursor()
        cursor.execute('DELETE FROM Room WHERE id = %s',int(id))
        db.commit()
        db.close()
        Delete_Device.check = True
        return webapp2.redirect('/delete-device')                  
            

