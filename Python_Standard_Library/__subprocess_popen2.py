
import subprocess

print 'popen2:'
proc = subprocess.Popen(
    ['cat', '-'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)


msg = 'throung stdin to stdout.'
stdout_value = proc.communicate(msg)
# stdout_value = proc.communicate(msg)[0]
print '\t pass throung:', repr(stdout_value)















