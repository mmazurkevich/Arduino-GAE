# -*- coding: utf-8 -*- 
import MySQLdb
import os
import sys
import webapp2
import time
import logging 
import controller.device_helper


class climateControl(webapp2.RequestHandler):

	fresh = []
	status = []
	warm = []
	temperature = 0
	check = True

	def control():
		curren_temperature = "запрос к бд"
		if (curren_temperature > (climateControl.temperature+1)):
			for a in fresh:
				if (deviceHelper.checkStatus(a)=="Off"):
					deviceHelper.ternOn(a) #включаем кондиционеры
			for a in warm:
				if (deviceHelper.checkStatus(a)=="On"):
					deviceHelper.ternOff(a)  #выключаем работающее тепловое оборудование
		elif (curren_temperature < (climateControl.temperature-1)):
			for a in warm:
				if (deviceHelper.checkStatus(a)=="Off"):
					deviceHelper.ternOn(a)
			for a in fresh:
				if (deviceHelper.checkStatus(a)=="On"):
					deviceHelper.ternOff(a)
		elif (curren_temperature>(climateControl.temperature-1) and curren_temperature<(climateControl.temperature+1)):
			for a in warm:
				if (deviceHelper.checkStatus(a)=="On"):
					deviceHelper.ternOff(a)
			for a in fresh:
				if (deviceHelper.checkStatus(a)=="On"):
					deviceHelper.ternOff(a)


	def get(self):
		'''global fresh,warm,status,temperature
		db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "temperature" OR devicetype = "heating" OR devicetype = "warm floor" OR devicetype = "air conditioner" ORDER BY devicetype')
		climatedevice = cursor.fetchall()
		#climateControl.temperature = int(param1)
		for onedevice in climatedevice:
			if (onedevice[1] == "temperature"):
				climateControl.status.append(int(onedevice[0]))
			if (onedevice[1] == "heating" or onedevice[1] == "warm floor"):
				climateControl.warm.append(int(onedevice[0]))
			if (onedevice[1] == "air conditioner"):
				climateControl.fresh.append(int(onedevice[0]))'''
		while (climateControl.check):
			logging.info("222")
			#control()
			time.sleep(5)
		'''if (climateControl.check == False):
			for a in warm:
				if (deviceHelper.checkStatus(a)=="On"):
					deviceHelper.ternOff(a)  #выключаем работающее тепловое оборудование
			for a in fresh:
				if (deviceHelper.checkStatus(a)=="On"):
					deviceHelper.ternOff(a)'''
			


