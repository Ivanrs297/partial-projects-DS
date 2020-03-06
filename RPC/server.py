# XML RPC Server

# open -a "Google Chrome" --args "file:///Users/reyes/Google%20Drive/CINVESTAV/2%20CUATRI/Sistemas%20Distribuidos/Felix/Proyectos/present.pdf#page=4"
# open -a "Google Chrome" "../present.pdf#page=4"
# open -a "Adobe Acrobat Reader DC" --args ../present.pdf

# open /Applications/Adobe\ Acrobat\ Reader\ DC.app/ --args "../present.pdf"

# open /Applications/Adobe\ Acrobat\ Reader\ DC.app/ --args '/A', 'page={4}', ../present.pdf
# open /Applications/Adobe\ Acrobat\ Reader\ DC.app/ --args /A "page={4}" "../present.pdf"

# open -a "Adobe Acrobat Reader DC" --args "file:///Users/reyes/Google%20Drive/CINVESTAV/2%20CUATRI/Sistemas%20Distribuidos/Felix/Proyectos/present.pdf#page=4"
# open -a "Adobe Acrobat Reader DC" --args "/A" "page={4}" "file:///Users/reyes/Google%20Drive/CINVESTAV/2%20CUATRI/Sistemas%20Distribuidos/Felix/Proyectos/present.pdf"
# open -a "Adobe Acrobat Reader DC" --args "../present.pdf"


from xmlrpc.server import SimpleXMLRPCServer
import os
import platform
from tinydb import TinyDB, Query

HOST = '10.0.5.234'
PORT = 4000

# Define Server
server = SimpleXMLRPCServer((HOST, PORT), logRequests=True, allow_none=True)

# Define functions 
class Course:

	''' CRUD of Course entity: '''

	def post(self, course = None):
		Course_query = Query()
		if db.search(Course_query.id == course['id']):
			return "Error, course ID already in DB"
		else:
			db.insert(course)
			return "Course Added"

	def get(self, id = None):
		if id:
			Course_query = Query()
			data = db.search(Course_query.id == id)
			return str(data)
		else:
			return str(db.all())

	def patch(self, id, key, value):
		Course_query = Query()
		if db.update({key: value}, Course_query.id == id):
			return "Modified"
		else:
			return "Error, course not found on DB"

	def delete(self, id):
		Course_query = Query()
		if db.remove(Course_query.id == id):
			return "Deleted"
		else:
			return "Error, course not found on DB"

	def drop(self):
		db.purge()
		return "DB deleted"

	def return_null(self):
		return None


def open_pdf(pdf_name, page):
	if platform.system() == "Darwin":
		cmd_string = f'open -a "Adobe Acrobat Reader DC" ../{pdf_name}.pdf'
	elif platform.system() == "Windows":
		cmd_string = f'AcroRd32.exe /A "page=5=OpenActions" ../{pdf_name}.pdf'
	os.system(cmd_string)

# Register functions
server.register_instance(Course())
server.register_function(open_pdf)

# Run program
if __name__ == '__main__':
	
	db = TinyDB('db.json')

	try:
		print(f"Server listenning on: {HOST}:{PORT}")
		server.serve_forever()
	except KeyboardInterrupt:
		print("Shuting down server...")