# -*- coding: utf-8 -*- 
import MySQLdb
import time
import webapp2
import logging
from controller.device_helper import deviceHelper



class autoLight(webapp2.RequestHandler):

	checkScript = True

	def get(self):
		db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "light"')
		lightDevice = cursor.fetchall()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "move"')
		sensorMove = cursor.fetchall()
		while (autoLight.checkScript):
			time.sleep(1)
			logging.info("111")
			for a in sensorMove:
				if (deviceHelper.checkSensor(deviceHelper,a[0]) == "On"): # посмотреть что датчик отдает
					for b in lightDevice:
						if (a[2] == b[2] and deviceHelper.checkStatus(deviceHelper,b[0])=="Off"):
							deviceHelper.ternOn(deviceHelper,b[0])  # задержка времени
				else:
					for b in lightDevice:
						if (a[2] == b[2] and deviceHelper.checkStatus(deviceHelper,b[0])=="On"):
							deviceHelper.ternOff(deviceHelper,b[0])	