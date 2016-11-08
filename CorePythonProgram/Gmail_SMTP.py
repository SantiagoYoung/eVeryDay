#!/usr/bin/env python
from cStringIO import StringIO
from platform import python_version

from imaplib import IMAP4_SSL
from poplib import POP3_SSL
from smtplib import SMTP


release = python_version()

if release > '2.6.2':
    from smtplib import SMTP_SSL
else:
    SMTP_SSL = None

Maibox = 'zswforyou'
passwd = 'yinxianjun'
who = 'zswforyou@gmail.com'
from_ = who
to = [who]

headers = [
    'From: %s' % from_,
    'To: %s'% ', '.join(to),
    'Subject: test SMTP send via 587/TLS',
    ]
body = [
    'Hello',
    'World!',
]
msg = '\r\n\r\n'.join(('\r\n'.join((headers)), '\r\n'.join(body)))

def getSubject(msg, default='(no subject line)'):
    for line in msg:
        if line.starswith('Subject:'):
            return line.rstrip()
        if not line:
            return default

s = SMTP_SSL('smtp.gmail.com', 587)

s.login(who, passwd)
s.sendmail(who, to, msg)
s.quit()




## POP
s = POP3_SSL('pop.gmail.com', 995)
s.user(who)
s.pass_(passwd)
rv, msg, sz = s.retr(s.stat()[0])
s.quit()
line = getSubject(msg)
print line
















