


import urllib


query_args ={'q':'query string', 'foo': 'bar'}
encoded_args = urllib.urlencode(query_args)
print 'Encoded:', encoded_args

url = 'http://localhost:8000/?' + encoded_args
# print urllib.urlopen(url).read()

query_args={'foo':['foo1', 'foo2']}
print 'Single:', urllib.urlencode(query_args)
print 'Sequence:', urllib.urlencode(query_args, doseq=True)

print '*' * 70
url = 'http://localhost:8000/'
print 'urlencode()  :', urllib.urlencode({'url':url})
print 'quote()  :', urllib.quote(url)
print 'quote_plus  :', urllib.quote_plus(url)
print '*' * 68
print urllib.unquote('http%3A%2F%2Flocalhost%3A8000%2F')
print urllib.unquote_plus('http%3A//localhost%3A8000/')









