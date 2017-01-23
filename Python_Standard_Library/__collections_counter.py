

from collections import Counter

print Counter(['a', 'b', 'c', 'b', 'b'])
print Counter({'a':2, 'b':3, 'c':1})
print Counter(a=2, b=3, c=1)

c = Counter()
print 'Initial:', c
c.update('abcdaadb')
print 'Sequence:', c
c.update({'a':1, 'd':5})
print 'Dict   :', c
print '*' * 58
c = Counter('abcdadba')
print c
for letter in 'abcde':
    print '%s: %d' % (letter, c[letter])
print '*' * 60
c = Counter('extremely')
c['z'] = 0
print c
print c.elements()
print list(c.elements())
print '*' * 60
print c.most_common()
print c.most_common(3)

print '*' *  60
c1 = Counter(['a', 'b', 'c', 'd', 'a', 'b', 'b'])
c2 = Counter('alphabet')
print 'C1: ', c1
print 'C2: ', c2

print '\nCombined counts: '
print c1 + c2

print '\nSubtraction: '
print c1 - c2

print '\nIntersection:'
print c1 & c2

print '\nUnion  :'
print c1 | c2
























