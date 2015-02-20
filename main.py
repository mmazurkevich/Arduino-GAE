import webapp2
from controller.index_controller import  Main, Light, Climate
from controller.settings_controller import  Main_Settings, Device_Settings
from controller.history_controller import  History



app = webapp2.WSGIApplication([
    	webapp2.Route(r'/', handler=Main, name=''),
    	webapp2.Route(r'/light', handler=Light, name=''),
    	webapp2.Route(r'/climate', handler=Climate, name=''),
    	#webapp2.Route(r'/security', handler=Security, name=''),
    	#webapp2.Route(r'/camera', handler=Camera, name=''),
        webapp2.Route(r'/settings', handler=Main_Settings, name=''),
        webapp2.Route(r'/add-device', handler=Device_Settings, name=''),
        webapp2.Route(r'/history', handler=History, name=''),
	], debug=True)
