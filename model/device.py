from google.appengine.ext import ndb

class Device(ndb.Model):
	pin = ndb.IntegerProperty()
	devicetype = ndb.StringProperty()
	roomname = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)