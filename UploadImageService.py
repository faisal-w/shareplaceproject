import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string

'''
class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", IndexHandler),
			(r"/upload", UploadHandler)
		]
		tornado.web.Application.__init__(self, handlers)
'''

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("tornado_upload.html")
 
class UploadHandler(tornado.web.RequestHandler):
	def post(self):
		file1 = self.request.files['file1'][0]
		original_fname = file1['filename']
 
		output_file = open("uploads/" + original_fname, 'wb')
		output_file.write(file1['body'])
	 
		self.finish("file " + original_fname + " is uploaded")
 
class ContentHandler:
	import pymongo, datetime
	connection = pymongo.Connection()

	def savePlacesToDB(data):
		db = connection['shareplaces_db']
		return null

	def createUploadDirectory(userId=None):
		if(userId==None):
			#save file to temporary example user directory
			print "Use example dir"
			strDateNow = ""
		else:
			print "use real dir"
			#save to real user directory 
			#create new directory by date
		return null

	def checkUser(userId):
		return null


settings = {
	'template_path': '',
	'static_path': 'static',
	"xsrf_cookies": False
}
 
application = tornado.web.Application([
	(r"/", IndexHandler),
	(r"/upload", UploadHandler) 
], debug=True,**settings)
 
print "Server started."
if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()