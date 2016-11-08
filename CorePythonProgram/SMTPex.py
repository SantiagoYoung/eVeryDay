#!/usr/bin/env python

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.163.com'
POP3SVR = 'pop.163.com'

who = 'santiago_young@163.com'
body = """
    From: %(who)s
    To: %(who)s
    Subject: test msg
    Hello World!
""" % {'who': who}


sendSvr = SMTP(SMTPSVR,25)
sendSvr.login(who, 'yinxianjun520')
errs = sendSvr.sendmail(who, [who], body)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)


recvSvr = POP3(POP3SVR)
recvSvr.user(who)
recvSvr.pass_('yinxianjun520')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])

sep = msg.index('')
recvBody = msg[sep+1:]
# assert body == recvBody
for line in recvBody:
    print line



























