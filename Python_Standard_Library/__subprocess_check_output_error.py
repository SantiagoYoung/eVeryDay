
import subprocess

try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell=True
    )
except subprocess.CalledProcessError as err:
    print 'Error:',err

else:
    print 'length:', len(output)
    print output



