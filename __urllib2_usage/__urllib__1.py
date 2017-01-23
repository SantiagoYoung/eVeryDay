
import urllib2


req = urllib2.Request('http://python.org')
response = urllib2.urlopen(req)
html = response.read()

print urllib2.urlopen('http://python.org').read()







