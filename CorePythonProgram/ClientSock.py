# -*- coding: utf8 -*-
#!/usr/bin/env python
'''
创建TCP客户端

cs = socket()
cs.connect()
comm_loop:
    cs.send()/cs.recv()
cs.close()

'''
from socket import *



HOST  = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')

    if not data:
        break
    tcpCliSock.send(data)

    print 'please waiting for response.'
    data = tcpCliSock.recv(BUFSIZ)
    print data

    if data:
        data = raw_input('> ')
        tcpCliSock.send(data)
    if not data:
        break
    print data
tcpCliSock.close()


