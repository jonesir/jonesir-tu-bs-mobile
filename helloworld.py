import sys
sys.path.insert(0,'libs')
from bs4 import BeautifulSoup 
import webapp2 
import urllib2

class MainPage(webapp2.RequestHandler):
    def get(self):
        html = urllib2.urlopen('https://www.tu-braunschweig.de/eitp/kontakt').read()
        soup = BeautifulSoup(html)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World! tubs\n')
        self.response.write(soup.get_text())
        
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)