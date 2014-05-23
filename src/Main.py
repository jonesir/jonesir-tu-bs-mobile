'''
Created on 22.05.2014

@author: jonesir
'''
import webapp2

html="<head><body>23.05.2014 jonesir</body></head>"
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(html)
        
app = webapp2.WSGIApplication([('/', MainPage)], debug = True)   