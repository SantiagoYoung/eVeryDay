


import collections


def default_factory():
    return 'default value'


d = collections.defaultdict()
print d
d = collections.defaultdict(default_factory, foo='bar')

print d
print 'foo =>', d['foo']
print 'bar ==>', d['bar']



d = collections.defaultdict(list)
print d['a']
d['a'] = 'A'
print d['a']

print d



















