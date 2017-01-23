
import os.path




for parts in [ ('one', 'two', 'three',),
               ('/', 'one', 'two', 'three'),
               ('/one', '/two', '/three'),]:
    print parts, ":", os.path.join(*parts)

for user in [ '', 'dhellmann', 'postgresql',]:
    lookup = '~' + user
    print '%12s : %s'  % (lookup, os.path.expanduser(lookup))

print '***' * 10
import os
os.environ['Myvar'] = 'value'
print os.path.expandvars('/path/to/$Myvar')
print "***" * 20
for path in ['one//two//three',
             'one/./two/./three',
             'one/../alt/two/three',]:
    print '%20s : %s' %(path, os.path.normpath(path))

print os.curdir
print os.pardir














