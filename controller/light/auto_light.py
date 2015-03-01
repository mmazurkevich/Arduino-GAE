# -*- coding: utf-8 -*- 
import MySQLdb
import time
import webapp2
import logging
from controller.device_helper import deviceHelper



class autoLight(webapp2.RequestHandler):

	checkScript = True

	def get(self):
		while (autoLight.checkScript):
			logging.info('1111')
			time.sleep(5)
		'''db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "light"')
		lightDevice = cursor.fetchall()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "move"')
		sensorMove = cursor.fetchall()
		while (autoLight.checkScript):
			for a in sensorMove:
				if (deviceHelper.checkSensor(a[0]) == "Сработал"): # посмотреть что датчик отдает
					for b in lightDevice:
						if (a[2] == b[2] and deviceHelper.checkStatus(b[0])=="Off"):
							deviceHelper.ternOn(b[0])  # задержка времени
				else:
					for b in lightDevice:
						if (a[2] == b[2] and deviceHelper.checkStatus(b[0])=="On"):
							deviceHelper.ternOff(b[0])	'''