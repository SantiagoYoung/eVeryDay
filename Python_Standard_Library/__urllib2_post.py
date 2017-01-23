


import urllib2
import urllib

query_args = {'q':'query string', 'foo': 'bar'}
encoded_args = urllib.urlencode(query_args)
url = 'http://localhost:8000/goods/collect_goods/'
print urllib2.urlopen(url, encoded_args).read()