import MySQLdb
import controller.device_helper

class Security():

	checkSecurity = True

	def get(self):
		db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
		cursor = db.cursor()
		cursor.execute('SELECT pin,devicetype,roomname FROM Device WHERE devicetype = "move",devicetype = "wet",devicetype = "reed"')
		houseSecure = cursor.fetchall()
		while (Security.checkSecurity):
			for a in houseSecure:
				if (a[1] == "wet"):
					if (deviceHelper.checkSensor(a[0]) == "Влажно"):
						Alarm_In_Room_Device_PIN
				if (a[1] == "move"):
					if (deviceHelper.checkSensor(a[0]) == "Движение"):
						Alarm_In_Room_Device_PIN
				if (a[1] == "reed"):
					if (deviceHelper.checkSensor(a[0]) == "Разомкнут"):
						Alarm_In_Room_Device_PIN
