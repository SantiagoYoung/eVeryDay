# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr))

sender = 'santiago_young@163.com'
passwd = 'yinxianjun520'
to_who = 'santiago_young@163.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('hello, send by Python..', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % sender)
msg['To'] = _format_addr('管理员 <%s>' % to_who)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server)
server.set_debuglevel(1)
server.login(sender, passwd)
server.sendmail(sender, [to_who], 'hello')
server.quit()

