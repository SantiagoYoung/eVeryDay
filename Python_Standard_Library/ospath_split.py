# coding=utf-8

import os.path


for path in ['/one/two/three', '/one/two/three/', '/','.','']:
    print '%15s : %s' % (path, os.path.split(path))

for path in ['/one/two/three', '/one/two/three/', '/', '.', '']:
    print '%15s : %s' % (path, os.path.basename(path))

for path in ['/one/two/three', '/one/two/three/', '/', '.', '']:
    print '%15s : %s' % (path, os.path.dirname(path))


for path in ['filename.txt', 'filename', '/path/to/filename.txt', '/', '', 'my-archive.tar.gz', 'no-extension.',]:
    print '%21s :' %  path, os.path.splitext(path)

print '**'*20
path = ['/one/two/three/four', '/one/two/threefold','/one/two/three/',]
print 'Prefix:', os.path.commonprefix(path)


print os.sep, '@@'
print os.extsep, '@@'