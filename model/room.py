from google.appengine.ext import ndb

class Room(ndb.Model):
	roomname = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)