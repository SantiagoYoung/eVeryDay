
import glob

for name in glob.glob('dir/*'):
    print name


print "Name explicitly:"
for name in glob.glob('dir/sudir/*'):
    print '\t', name

print 'Name with wildcard:'
for name in glob.glob('dir/*/*'):
    print '\t', name

print '***'*20

for name in glob.glob('dir/file?.txt'):
    print name
print '***'*20
for name in glob.glob('dir/*[0-9].*'):
    print name