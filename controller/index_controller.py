import jinja2
import os
import webapp2
import MySQLdb
import logging   # console loglib
import json



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/home/view')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) 

class Main(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('room_plan.html')
        self.response.out.write(template.render())


