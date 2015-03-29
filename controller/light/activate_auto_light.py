import webapp2

from google.appengine.api import taskqueue
from auto_light import autoLight
from controller.climate.climate_control import climateControl
from controller.security.secur import Security
from controller.device_helper import deviceHelper

class activateAutoLight(webapp2.RequestHandler):

	def get(self):
		if (self.request.GET['type'] == "On"):
			if (self.request.GET['name'] == "light"):
				info = "Tern on auto light"
				deviceHelper.addToBD(deviceHelper,99,info)
				autoLight.checkScript = True
				taskqueue.add(url='/light/auto-light',queue_name='light', method='GET')
			if (self.request.GET['name'] == "climate"):
				info = "Tern on climate control"
				deviceHelper.addToBD(deviceHelper,99,info)
				climateControl.check = True
				taskqueue.add(url='/climate/control',queue_name='climate', method='GET')
			if (self.request.GET['name'] == "secure"):
				info = "Tern on security"
				deviceHelper.addToBD(deviceHelper,99,info)
				Security.checkSecurity = True
				taskqueue.add(url='/security',queue_name='default', method='GET')

		if (self.request.GET['type'] == "Off"):
			if (self.request.GET['name'] == "light"):
				info = "Tern off auto light"
				deviceHelper.addToBD(deviceHelper,99,info)				
				autoLight.checkScript = False
			if (self.request.GET['name'] == "climate"):
				info = "Tern off climate control"
				deviceHelper.addToBD(deviceHelper,99,info)				
				climateControl.check = False
			if (self.request.GET['name'] == "secure"):
				info = "Tern off security"
				deviceHelper.addToBD(deviceHelper,99,info)				
				Security.checkSecurity = False
			
			#q = taskqueue.Queue('default')
        	#q.purge()