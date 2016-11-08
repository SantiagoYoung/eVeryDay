# -*- coding: utf-8 -*-
# import socket

# socket(socket_family, socket_type, protocol=0)

# TCP/IP套接字
# tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# UDP/IP 套接字
# udpSock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)



'''
from socket import socket
ss = socket(AF_INET, SOCK_STREAM)  创建套接字
ss.bind()                          套接字与地址绑定
ss.listen()                        监听链接
inf_loop：                         服务器无线循环
    cs = ss.accept()               接受客户端链接
    comm_loop:                     通信循环
        cs.recv()/cs.send()        对话（接受/发送）
    cs.close()                     关闭客户端套接字
ss.close()                         关闭服务器端套接字
'''


from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerScok = socket(AF_INET, SOCK_STREAM)
tcpSerScok.bind(ADDR)
tcpSerScok.listen(5)
try:
    while True:
        print 'waiting for connection....'
        tcpCliSock, addr = tcpSerScok.accept()
        print tcpCliSock, addr
        print '.....connected from:', addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            print data
            if data:
                send_msg = raw_input('> ')
                tcpCliSock.send('%s: %s' % ('neon', send_msg))
            if not data:
                break
            # tcpCliSock.send('[%s] %s' %(
            #     ctime(), data ))
        tcpCliSock.close()
except (EOFError, KeyboardInterrupt):
    tcpSerScok.close()









































