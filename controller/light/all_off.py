import MySQLdb
import webapp2
from controller.device_helper import deviceHelper


class allOff(webapp2.RequestHandler):

	def get(self):
		db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "light"')
		lightDevice = cursor.fetchall()
		info = "Tern off light everywhere"
		deviceHelper.addToBD(deviceHelper,99,info)		
		for b in lightDevice:
			if (deviceHelper.checkStatus(deviceHelper,b[0]) == "On"):
				deviceHelper.ternOff(deviceHelper,b[0])

