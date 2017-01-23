import os

from urllib import pathname2url, url2pathname


print ' == Default ==='
path = '/a/b/c'
print 'Original:', path
print 'URL     :', pathname2url(path)
print 'Patch   :', url2pathname('/d/e/f')
print

from nturl2path import pathname2url, url2pathname

print ' == Windows, without drive letter =='
path = r'\a\b\c'
print 'Original:', path
print 'URL   :', pathname2url(path)
print 'Path   :', url2pathname('/d/e/f')
print


print  '== Windows, with drive letter =='
path = r'C:\a\b\c'
print 'Original:', path
print 'URL   :', pathname2url(path)
print 'Path   :', url2pathname('/d/e/f')



