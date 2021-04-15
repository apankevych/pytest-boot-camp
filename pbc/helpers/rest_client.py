import httpx

class restcl(object):
	
	def __init__(self):
		#self.hostname = hostname
		#self.port = port
		self.connect()
		self.cl = None
		
	def connect(self):
		self.cl = httpx.Client()
		
	def get(self, host, port, schema = 'http'):
		url = '{}://{}:{}'.format(schema, host, port)
		return httpx.get(url)
		
