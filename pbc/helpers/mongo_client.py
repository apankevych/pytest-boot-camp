import pymongo

class mongocl(object):
	
	def __init__(self, hostname, port):
		self.hostname = hostname
		self.port = port
		self.connect()
		self.cl = None
		self.db = None
		
	def connect(self):
		self.cl = pymongo.MongoClient('mongodb://{}:{}/'.format(self.hostname, self.port))
		
	def get_one(self, db, post_id):
		post = self.cl.db.posts.find_one({'_id': ObjectId(post_id)})
		
