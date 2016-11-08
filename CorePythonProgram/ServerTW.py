#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime
import os



PORT = 21567
class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        client = self.client = self.transport.getPeer().host
        print '.....connected from :', client

    def dataReceived(self, data):
        L = data.split(' ')
        print L

        if L[0] == 'ls':
            self.transport.write("%s" % os.listdir(L[1]))
        if data == 'date':
            self.transport.write('%s' % ctime())
        if data == 'ls':
            self.transport.write('%s' % os.listdir(os.curdir))
        if data == 'os':
            self.transport.write('%s' % os.name)
        else:
            self.transport.write('[%s] %s' %(ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServerProtocol
print 'waiting for connectin..'
reactor.listenTCP(PORT, factory)
reactor.run()






















