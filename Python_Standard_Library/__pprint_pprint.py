
from pprint_data import data

from pprint import pprint



print  'Print:'
print data

print
print 'PPRINT:'
pprint(data)
print '*' * 80


local_data = ['a','b', 1, 2]
print  'local data:', local_data
local_data.append(local_data)
print local_data

print 'id(local_data) =>', id(local_data)
pprint(local_data, depth=1)

pprint(data, depth=1)