''' NOTE: This does not work (assumedly because of protections on the page).'''

from bs4 import BeautifulSoup
import urllib2
import re
import json
import sys
import mechanize
import cookielib

url = 'http://tenders.gov.in/innerpage.asp?choice=ct1&page=9'

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
#br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

LoginHeader = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}


br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)'), ("Referer", "http://tenders.gov.in/innerpage.asp?choice=as0")]

'''opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
f = opener.open(url)
'''


#req = urllib2.Request(url=url)
r = br.open(url)
html = r.read()
print html

exit()

#f = urllib2.urlopen(req)


page = BeautifulSoup(f.read())
print page.prettify()
exit()


def clean(s):
    s = s.strip().replace('\n', '').replace('\r', '')
    s = s.replace(':', '').strip()
    s = re.sub(r"( )+", ' ', s)
    return s

for td in page.findAll('td', { "class" : "TabBodyBrdrLess" }):
    for t in td.find_all('a'):
        print t
'''
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
                print json.dumps(jr)'''
