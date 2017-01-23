


import os

print 'Inital value:', os.environ.get('TESTVAR', None)
print 'Child process:',
os.system('echo $TESTVAR')

os.environ['TESTVAR'] = 'THIS VALUE WAS CHANGED.'

print
print 'Changed value:', os.environ['TESTVAR']
print 'Child process:',
os.system('echo $TESTVAR')

print
print 'Removed value:', os.environ.pop('TESTVAR', None)
print 'Child process:',
os.system('echo $TESTVAR')

