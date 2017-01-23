

import subprocess

subprocess.call(['ls','-l'])

subprocess.call('echo $HOME', shell=True)


try:
    subprocess.check_call(['false'])
except subprocess.CalledProcessError as err:
    print 'Error:', err


print '**' * 30

output = subprocess.check_output(['ls','-l'])
print 'length %s' % len(output)
print output