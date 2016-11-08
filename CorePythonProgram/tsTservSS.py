# -*-coding: utf-8 -*-
#!/usr/bin/env python
import SocketServer
from SocketServer import (TCPServer ,
                          StreamRequestHandler as SRH)
from time import ctime


HOST = ''
PORT = 10002
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):

    def handler(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' %(ctime(),
                                           self.rfile.readline()))
tcpServ = SocketServer.ThreadingTCPServer(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()








