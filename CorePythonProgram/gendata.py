

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxint
from time import ctime



tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in xrange(randrange(5, 11)):

    dtint = randrange(maxint/998)

    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in xrange(dlen))
    '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom,
                                      choice(tlds), dtint, llen, dlen)




import re
print re.match('(ba|bi|bu|ha|hi|hu)t', 'but').group(1)

data = 'hello world'
print re.match(r'(\w+) (\w+)', data).group()
print re.match(r'(\w+) (\w+)', data).groups()
data = 'neon,god'
print re.match(r'(\w+)[, ](\w+)', data).group()
print re.match(r'(\w+)[, ](\w+)', data).groups()

print re.match(r'^[\w_][\w\d_]*', data).group()

data = '1180 Bordeaux Drive'
print re.match((r'(\d)+ (\w)+ (\w)+'), data).group()
print re.match((r'(\d+) (\w+) (\w+)'), data).groups()

data = 'www://www.yahoo.com'
print re.match(r'^(www)://(www.)*(\w){3,9}\.(com|edu|net|cn)$', data).group()
print re.match(r'^(www)://(www.)*(\w{3,9})\.(com|edu|net|cn)$', data).groups()

num = str(13556156) +'L'

# print re.match((r'(\d+)\d$'), num).group()
print re.match(r'(\d+)[Ll]$', num).group()
num = '1.123'
print re.match(r'(\d*).(\d*)', num).group()

# email = re.match(r'^[\d\w](.*)@([\w\d]{2,9})\.(com|cn|)')

# url = re.match(r'^(http|https)://www\.(.*)\.(com|cn|edu|net)')

data = str(type(dir))
print data
print re.search(r"'.*'", data).group()


cal = '2016.11'
print re.match(r'\d{4}\.1?[1-9]', cal).group()








