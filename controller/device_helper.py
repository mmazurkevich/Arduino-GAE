import webapp2

class deviceHelper(webapp2.RequestHandler): 
	
	def get(self):
		pin = self.request.GET['pin']
		if (self.request.GET['type']=='On'):
			self.ternOn(pin)
		if (self.request.GET['type']=='Off'):
			self.ternOff(pin)
		if (self.request.GET['type']=='CheckStatus'):
			self.checkStatus(pin)
		if (self.request.GET['type']=='CheckSensor'):
			self.checkSensor(pin)

	def checkStatus(self,pin):
		return 1  # On or Off return

	def checkSensor(self,pin):
		return 1  # On or Off return

	def ternOff(self,pin):
		return 1

	def ternOn(self,pin):
		return 1

		    #def post(self):
		#	url = "https://api.github.com/"
		#	res = urlfetch.fetch(url)
		#	if res.status_code == 200:
		#		mom = "ssdsd"
		#		top = "44434"
		#		lol = mom + top + '\n'
		#		for i in range(5):
		#			self.response.write(lol)
		#		#logging.info(res.content)
		#		j = json.loads(res.content)
	  	#		self.response.write(j['starred_url'])