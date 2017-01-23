

import os

print  'popen, read:',

stdout = os.popen('echo "to stdout"', 'r')

try:
    stdout_value = stdout.read()
finally:
    stdout.close()

print '\tstdout:', repr(stdout_value)

print '\npopen, write:'
stdin = os.popen('cat -', 'w')

try:
    stdin.write('\tstdin: to std\n')
finally:
    stdin.close()

print os.path.join(__name__)


print os.path.abspath(os.path.dirname(__file__))



print os.path.dirname(__file__)

