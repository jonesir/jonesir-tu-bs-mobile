import sys
import json
sys.path.insert(0,'libs')
from bs4 import BeautifulSoup 
import webapp2 
import urllib2

HOST_TU_BS = 'https://www.tu-braunschweig.de/'
# url as constants for request
FAKULTAET_1 = HOST_TU_BS + 'fk1'
FAKULTAET_2 = HOST_TU_BS + 'flw'
FAKULTAET_3 = HOST_TU_BS + 'abu'
FAKULTAET_4 = HOST_TU_BS + 'fmb'
FAKULTAET_5 = HOST_TU_BS + 'eitp'
FAKULTAET_6 = HOST_TU_BS + 'fk6'

class Fakultaeten(webapp2.RequestHandler):
#     options = {"1":fakultaet1, "2":fakultaet2, "3":fakultaet3, "4":fakultaet4, "5":fakultaet5, "6":fakultaet6}
    
    def get(self):
        # specify that the response is in of format 'json'
        self.response.headers['Content-Type'] = 'application/json'
        
        # get fakultaet number
        fakultaet = int(self.request.url[len(self.request.host_url)+len('/fakultaeten/'):])
        
        # do corresponding stuff according to fakultaet
        if fakultaet == 1:
            self.fakultaet1()
        elif fakultaet == 2:
            self.fakultaet2()
        elif fakultaet == 3:
            self.fakultaet3()
        elif fakultaet == 4:
            self.fakultaet4()
        elif fakultaet == 5:
            self.fakultaet5()
        elif fakultaet == 6:
            self.fakultaet6()
            
        # create and generate json string
        result_json = {'fakultaet':fakultaet}
        jsonString = json.dumps(result_json)
        
    # Carl-Friedrich-Gauss-Fakultaet    
    def fakultaet1(self):
        html = urllib2.urlopen(FAKULTAET_1).read()
        soup = BeautifulSoup(html)
        self.response.write(soup.prettify())
        
    # Lebenswissenschaften
    def fakultaet2(self):
        html = urllib2.urlopen(FAKULTAET_2).read()
        soup = BeautifulSoup(html)
        self.response.write(soup.prettify())
    
    # Architektur, Bauingenieurwesen und Umweltwissenschaften
    def fakultaet3(self):
        html = urllib2.urlopen(FAKULTAET_3).read()
        soup = BeautifulSoup(html)
        self.response.write(soup.prettify())
        
    # Elektrotechnik, Informationstechnik, Physik
    def fakultaet4(self):
        html = urllib2.urlopen(FAKULTAET_4).read()
        soup = BeautifulSoup(html)
        self.response.write(soup.prettify())
        
    # Geistes- und Erziehungswissenschaften
    def fakultaet5(self):
        html = urllib2.urlopen(FAKULTAET_5).read()
        soup = BeautifulSoup(html)
        self.response.write(soup.prettify())
        
    def fakultaet6(self):
        html = urllib2.urlopen(FAKULTAET_6).read()
        soup = BeautifulSoup(html)
        self.response.write(soup.prettify())
        
application = webapp2.WSGIApplication([
    ('/fakultaeten/.*', Fakultaeten),
], debug=True)