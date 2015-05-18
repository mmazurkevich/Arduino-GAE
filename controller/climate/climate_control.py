# -*- coding: utf-8 -*- 
import MySQLdb
import os
import sys
import webapp2
import time
from controller.device_helper import deviceHelper
import json
import logging 
from google.appengine.api import urlfetch


class climateControl(webapp2.RequestHandler):

	fresh = []
	status = []
	warm = []
	temperature = 0
	check = True

	@staticmethod
	def control(self):
		curren_temperature = deviceHelper.checkHumTemp(deviceHelper,"temperature")
		if (curren_temperature > (climateControl.temperature+1)):
			for a in climateControl.fresh:
				if (deviceHelper.checkStatus(deviceHelper,a)=="Off"):
					deviceHelper.ternOn(deviceHelper,a) #включаем кондиционеры
			for a in climateControl.warm:
				if (deviceHelper.checkStatus(deviceHelper,a)=="On"):
					deviceHelper.ternOff(deviceHelper,a)  #выключаем работающее тепловое оборудование
		elif (curren_temperature < (climateControl.temperature-1)):
			for a in climateControl.warm:
				if (deviceHelper.checkStatus(deviceHelper,a)=="Off"):
					deviceHelper.ternOn(deviceHelper,a)
			for a in climateControl.fresh:
				if (deviceHelper.checkStatus(deviceHelper,a)=="On"):
					deviceHelper.ternOff(deviceHelper,a)
		elif (curren_temperature>(climateControl.temperature-1) and curren_temperature<(climateControl.temperature+1)):
			for a in climateControl.warm:
				if (deviceHelper.checkStatus(deviceHelper,a)=="On"):
					deviceHelper.ternOff(deviceHelper,a)
			for a in climateControl.fresh:
				if (deviceHelper.checkStatus(deviceHelper,a)=="On"):
					deviceHelper.ternOff(deviceHelper,a)


	def get(self):
		global fresh,warm,status,temperature
		db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "temperature" OR devicetype = "heating" OR devicetype = "warm floor" OR devicetype = "air conditioner" ORDER BY devicetype')
		climatedevice = cursor.fetchall()
		climateControl.temperature = int(self.request.GET['count']) # забирать значение с пользовательского интерфейса.
		for onedevice in climatedevice:
			if (onedevice[1] == "temperature"):
				climateControl.status.append(int(onedevice[0]))
			if (onedevice[1] == "heating" or onedevice[1] == "warm floor"):
				climateControl.warm.append(int(onedevice[0]))
			if (onedevice[1] == "air conditioner"):
				climateControl.fresh.append(int(onedevice[0]))
		while (climateControl.check):
			logging.info("222")
			climateControl.control(climateControl)
			time.sleep(2)
		if (climateControl.check == False):
			for a in climateControl.warm:
				if (deviceHelper.checkStatus(deviceHelper,a)=="On"):
					deviceHelper.ternOff(deviceHelper,a)  #выключаем работающее тепловое оборудование
			for a in climateControl.fresh:
				if (deviceHelper.checkStatus(deviceHelper,a)=="On"):
					deviceHelper.ternOff(deviceHelper,a)
			


