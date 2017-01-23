


import urllib2

response = urllib2.urlopen('http://localhost:8000/')
print 'RESPONSE:', response

# for line in response:
#     print line.rstrip()

print 'URL     :', response.geturl()



headers = response.info()
print 'DATE :', headers['date']
print 'HEADERS :'
print '_________'
print headers


data = response.read()
print 'LENGTH  :', len(data)
print 'DATA  :'
print '__________'
print data