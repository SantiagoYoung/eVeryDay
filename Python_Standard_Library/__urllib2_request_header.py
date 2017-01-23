


import urllib2


request = urllib2.Request('http://localhost:8000')
request.add_header(
    'User-agent',
    'PyMOTW (http://www.doughellmann.com/PyMOTW)',
)

response = urllib2.urlopen(request)

print response.read()