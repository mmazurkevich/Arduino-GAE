import webapp2

from google.appengine.api import taskqueue
from auto_light import autoLight
from controller.climate.climate_control import climateControl
from controller.security.secur import Security

class activateAutoLight(webapp2.RequestHandler):

	def get(self):
		if (self.request.GET['type'] == "On"):
			if (self.request.GET['name'] == "light"):
				autoLight.checkScript = True
				taskqueue.add(url='/light/auto-light',queue_name='light', method='GET')
			if (self.request.GET['name'] == "climate"):
				climateControl.check = True
				taskqueue.add(url='/climate/control',queue_name='climate', method='GET')
			if (self.request.GET['name'] == "secure"):
				Security.checkSecurity = True
				taskqueue.add(url='/security',queue_name='default', method='GET')

		if (self.request.GET['type'] == "Off"):
			if (self.request.GET['name'] == "light"):
				autoLight.checkScript = False
			if (self.request.GET['name'] == "climate"):
				climateControl.check = False
			if (self.request.GET['name'] == "secure"):
				Security.checkSecurity = False
			
			#q = taskqueue.Queue('default')
        	#q.purge()