import MySQLdb
import webapp2
import logging 
from controller.device_helper import deviceHelper

class RoomLight(webapp2.RequestHandler):

	def get(self):
		db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE roomname = %s AND devicetype = "light" ',self.request.GET['room'])
		roomLightDevice = cursor.fetchall()
		if (self.request.GET['type']=='On'):
			info = "Tern on light in room " + self.request.GET['room']
			deviceHelper.addToBD(deviceHelper,99,info)			
			for oneDevice in roomLightDevice:
				if (deviceHelper.checkStatus(deviceHelper,oneDevice[0])=="Off"):
					deviceHelper.ternOn(deviceHelper,oneDevice[0])
		if (self.request.GET['type']=='Off'):
			info = "Tern off light in room " + self.request.GET['room']
			deviceHelper.addToBD(deviceHelper,99,info)			
			for oneDevice in roomLightDevice:
				if (deviceHelper.checkStatus(deviceHelper,oneDevice[0])=="On"):
					deviceHelper.ternOff(deviceHelper,oneDevice[0])


