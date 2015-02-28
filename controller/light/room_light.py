import MySQLdb
import webapp2
import logging 
from controller.device_helper import deviceHelper

class RoomLight(webapp2.RequestHandler):

	def get(self):
		room = self.request.GET['room']
		db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "light", roomname = room')
		roomLightDevice = cursor.fetchall()
		if (self.request.GET['type']=='On'):
			for oneDevice in roomLightDevice:
				if (deviceHelper.checkStatus(oneDevice[0])=="Off"):
					deviceHelper.ternOn(oneDevice[0])
		if (self.request.GET['type']=='Off'):
			for oneDevice in roomLightDevice:
				if (deviceHelper.checkStatus(oneDevice[0])=="On"):
					deviceHelper.ternOff(oneDevice[0])


