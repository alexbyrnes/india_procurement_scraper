from bs4 import BeautifulSoup
import urllib2
import re
import json
import sys


choice = sys.argv[1]
tid = sys.argv[2]

#req = urllib2.Request(url='http://tenders.gov.in/innerpage.asp?choice=ct1&page=9')
req = urllib2.Request(url='http://tenders.gov.in/innerpage.asp?choice=tc5&tid=chd574866&work=1')
req = urllib2.Request(url='http://tenders.gov.in/innerpage.asp?choice=%s&tid=%s&work=1' % (choice, tid))
f = urllib2.urlopen(req)
page = BeautifulSoup(f.read())

def clean(s):
    s = s.strip().replace('\n', '').replace('\r', '')
    s = s.replace(':', '').strip()
    s = re.sub(r"( )+", ' ', s)
    return s

for table in page.find_all('form', { "name" : "displayform" }):
    for t in table.find_all('table'):
        for row in table.find_all('tr'):
            data = []
            for td in row.find_all('td'):
                datum = td.get_text()
                datum = clean(datum)
                data.append(datum)

            fieldname = data[0]
            if fieldname != '' and len(data) > 1:
                jr = {}
                jr[fieldname] = data[1]
                print json.dumps(jr)
