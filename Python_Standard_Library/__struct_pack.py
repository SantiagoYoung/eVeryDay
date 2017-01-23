

import struct
import binascii



values = (1, 'ab', 2.4)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print 'Original values:', values
print 'Format string:', s.format
print 'Uses :', s.size,'bytes'
print 'Packed Value:', binascii.hexlify(packed_data)


packed_data = binascii.unhexlify('0100000061620000cdcc2c40')

unpacked_data = s.unpack(packed_data)
print "Unpacked Values:", unpacked_data




