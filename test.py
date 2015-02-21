import MySQLdb
import os

db = MySQLdb.connect(host='127.0.0.1', port=3306, db='home', user='root', passwd='')
cursor = db.cursor()
cursor.execute('SELECT roomname FROM Room')
room = cursor.fetchall()
for a in room:
	print a[0]