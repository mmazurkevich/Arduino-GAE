from google.appengine.ext import ndb

class Type(ndb.Model):
	devicetype = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)