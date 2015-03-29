import webapp2
from controller.device_helper import  deviceHelper
from controller.light.light import Light
from controller.light.all_off import allOff
from controller.light.room_light import RoomLight
from controller.light.auto_light import autoLight
from controller.light.activate_auto_light import activateAutoLight
from controller.climate.climate import  Climate
from controller.climate.climate_control import climateControl
from controller.security.secur import  Security
from controller.index_controller import  Main
from controller.settings.settings_controller import  Main_Settings, Delete_Device, Delete, Delete1, Delete2

app = webapp2.WSGIApplication([
    	webapp2.Route(r'/', handler=Main, name=''),
    	webapp2.Route(r'/light', handler=Light, name=''),
    	webapp2.Route(r'/light/room-light', handler=RoomLight, name=''),
    	webapp2.Route(r'/light/all-off', handler=allOff, name=''),
    	webapp2.Route(r'/light/activate-auto', handler=activateAutoLight, name=''),
    	webapp2.Route(r'/light/auto-light', handler=autoLight, name=''),
    	webapp2.Route(r'/climate', handler=Climate, name=''),
    	webapp2.Route(r'/climate/control', handler=climateControl, name=''),
    	webapp2.Route(r'/security', handler=Security, name=''),
    	#webapp2.Route(r'/camera', handler=Camera, name=''),
        webapp2.Route(r'/settings', handler=Main_Settings, name=''),
        webapp2.Route(r'/delete-device', handler=Delete_Device, name=''),
        webapp2.Route(r'/delete-device/<id:\d+>', handler=Delete, name=''),
        webapp2.Route(r'/delete-type/<id:\d+>', handler=Delete1, name=''),
        webapp2.Route(r'/delete-room/<id:\d+>', handler=Delete2, name=''),        
        webapp2.Route(r'/device-helper', handler=deviceHelper, name=''),
        
	], debug=True)
