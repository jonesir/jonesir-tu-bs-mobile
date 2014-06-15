import sys
sys.path.insert(0,'libs')
from bs4 import BeautifulSoup 
import webapp2 
import urllib2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hallo, Willkommen bei Mobile TU Braunschweig.')
        
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)