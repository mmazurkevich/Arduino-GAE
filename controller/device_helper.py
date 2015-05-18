# -*- coding: utf-8 -*- 
import webapp2
import urllib2
import MySQLdb
import json
import logging 
from google.appengine.api import urlfetch

class deviceHelper(webapp2.RequestHandler): 
	
	ip = "192.168.0.2" #Брать IP откуда нибудь
	
	def get(self):
		pin = self.request.GET['pin']
		if (self.request.GET['type']=='On'):
			self.ternOn(self,pin)
		if (self.request.GET['type']=='Off'):
			self.ternOff(self,pin)

	@staticmethod
	def addToBD(self,pin,info):
		db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('INSERT INTO History (pin,info,user) VALUES (%s,%s,%s)',(pin,info,"admin"))
		db.commit()
		db.close()		

	@staticmethod
	def setMode(self,pin,mode):
		url = "http://"+deviceHelper.ip+"/mode/"+str(pin)+"/"+mode
		result = urlfetch.fetch(url)
		info = "Add new device PIN "+str(pin)
		deviceHelper.addToBD(deviceHelper,pin,info)		

	@staticmethod
	def checkStatus(self,pin):
		url = "http://"+deviceHelper.ip+"/digital/"+str(pin)
		result = urlfetch.fetch(url)
		data = json.loads(result.content)
		if (data["return_value"] == 0):
			res = "On"
		else:
			res = "Off"
		return res  # On or Off return

	@staticmethod
	def checkSensor(self,pin):
		url = "http://"+deviceHelper.ip+"/digital/"+str(pin)
		result = urlfetch.fetch(url)
		data = json.loads(result.content)
		if (data["return_value"] == 1):
			res = "On"
		else:
			res = "Off"
		return res  # On or Off return

	@staticmethod
	def ternOff(self,pin):
		url = "http://"+deviceHelper.ip+"/digital/"+str(pin)+"/"+"1"
		result = urllib2.urlopen(url)
		info = "Tern off device PIN "+str(pin)
		deviceHelper.addToBD(deviceHelper,pin,info)	

	@staticmethod
	def ternOn(self,pin):
		url = "http://"+deviceHelper.ip+"/digital/"+str(pin)+"/"+"0"
		result = urllib2.urlopen(url)
		info = "Tern on device PIN "+str(pin)
		deviceHelper.addToBD(deviceHelper,pin,info)		
	
	@staticmethod
	def	checkHumTemp(self,name):	
		url = "http://"+deviceHelper.ip+"/update?l=0"
		result = urlfetch.fetch(url)
		if (name == "humidity" ):
			url = "http://"+deviceHelper.ip+"/humidity"
			result = urlfetch.fetch(url)
			data = json.loads(result.content)
			return data["humidity"]
		if (name == "temperature"):
			url = "http://"+deviceHelper.ip+"/temperature"
			result = urlfetch.fetch(url)
			data = json.loads(result.content)
			return data["temperature"]	
