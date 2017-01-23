
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

output = StringIO()
output.write('This goes into the buffer.')
print >>output, 'And so does this.'

print output.getvalue()

output.close()

input = StringIO('Inital value for read buffer.'
                 ' g g g g g ')
print input.getvalue()
# print input.read()

# print input.readline()
print input.readlines()































