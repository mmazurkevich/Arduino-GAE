import jinja2
import os
import webapp2
import logging   # console loglib
import json

from google.appengine.api import urlfetch  # request  lib 


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'/home/infinity/google_appengine/home/view')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) 


class History(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('history.html')
        self.response.out.write(template.render())