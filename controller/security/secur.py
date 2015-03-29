# -*- coding: utf-8 -*- 
import MySQLdb
import logging
import webapp2
import time
from controller.device_helper import deviceHelper
import json
import logging 
from google.appengine.api import urlfetch

class Security(webapp2.RequestHandler):

	checkSecurity = True

	def get(self):
		db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "move" OR devicetype = "humidity" OR devicetype = "reed"')
		houseSecure = cursor.fetchall()
		logging.info("3адержка")
		time.sleep(10) # задержка до постановки на охрану
		logging.info("Старт")
		while (Security.checkSecurity):
			logging.info("333")
			time.sleep(1)
			for a in houseSecure:
				if (a[1] == "humidity"):
					if (deviceHelper.checkHumTemp(deviceHelper,"humidity") > 90):
						url = "http://sms.ru/sms/send?api_id=51a2c6e5-e117-2764-5d9a-03e5b38176f6&to=79307700396&text=Сработал+датчик+влажности+в+комнате+"+a[2]
						result = urlfetch.fetch(url)
						Security.checkSecurity = False
				if (a[1] == "move"):
					if (deviceHelper.checkSensor(deviceHelper,a[0]) == "On"):
						url = "http://sms.ru/sms/send?api_id=51a2c6e5-e117-2764-5d9a-03e5b38176f6&to=79307700396&text=Сработал+датчик+движения+в+комнате+"+a[2]
						result = urlfetch.fetch(url)
						Security.checkSecurity = False	
				if (a[1] == "reed"):
					if (deviceHelper.checkSensor(deviceHelper,a[0]) == "Off"):
						url = "http://sms.ru/sms/send?api_id=51a2c6e5-e117-2764-5d9a-03e5b38176f6&to=79307700396&text=Открыта+дверь+в+комнате+"+a[2]
						result = urlfetch.fetch(url)
						Security.checkSecurity = False	
