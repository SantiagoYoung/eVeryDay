
import subprocess

print 'read:'
proc = subprocess.Popen(['echo', '"to stdout"'],
                        stdout=subprocess.PIPE)

stdout_value = proc.communicate()[0]
print '\tstdout:', repr(stdout_value)

print  '**' * 30
print 'write:'

proc = subprocess.Popen(['cat','-'],
                        stdin=subprocess.PIPE)
# stdin_value = proc.communicate()
# print stdin_value
stdin_value = proc.communicate('\tstadin: to stdin\n')






