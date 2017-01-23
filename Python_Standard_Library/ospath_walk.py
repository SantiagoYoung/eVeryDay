
import os
import os.path
import pprint

def visit(arg, dirname, names):
    print dirname, arg, names
    for name in names:
        subname = os.path.join(dirname, name)
        if os.path.isdir(subname):
            print ' %s/'%name
        else:
            print ' %s/'%name
    print

if not os.path.exists('example'):
    os.mkdir('example')
if not os.path.exists('example/one'):
    os.mkdir('example/one')

with open('example/one/file.txt', 'wt') as f:
    f.write('contents')
with open('example/two.txt', 'wt') as f:
    f.write('contents')

os.path.walk('example', visit, '(User date)')
