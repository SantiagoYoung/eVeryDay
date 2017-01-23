

import collections

Person = collections.namedtuple('Person', 'name age gender')
print 'Type of Person:', type(Person)
print Person

bob = Person(name='Bob', age=30, gender='male')
print 'Representation:', bob

jane = Person(name='Jane', age=29, gender='female')
print 'Field by name:', jane.name

print 'Field by index:'
for p in [bob, jane]:
    print '%s is a %d year old %s' % p

print '*' * 80
with_class = collections.namedtuple('Person', 'name class age gender', rename=True)

print with_class._fields

two_age = collections.namedtuple('Person', 'name name age gender gender age', rename=True)

print two_age._fields












