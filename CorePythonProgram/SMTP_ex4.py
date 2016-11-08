#!/usr/bin/env python

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import email as Email
def processMsg(msg):
    body = ''
    msg = Email.message_from_string(msg)
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload()
                break
            else:
                body = msg.get_payload(decode=True)
    else:
        body = msg.get_payload(decode=True)

    return body






def make_mpa_msg():
    email = MIMEMultipart('alterntive')
    text = MIMEText('Hello world.\r\n', 'plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>Hello World!</h4>'
        '<body></html>', 'html'
    )
    email.attach(html)

    return email

def make_img_msg(fn):
    f = open(fn, 'r')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition',
                     'attachment; filename="%s"' %fn)
    return email

def sendMsg(fr, to, msg):
    s = SMTP('smtp.163.com')
    s.login( 'santiago_young@163.com','yinxianjun520')
    errs = s.sendmail(fr, to, msg)
    s.quit()


if __name__ == '__main__':
    print 'hello sending is start'
    SENDER = 'santiago_young@163.com'
    RECIPS = 'santiago_young@163.com'
    msg = make_mpa_msg()
    msg['FROM'] = SENDER
    msg['TO'] = ', '.join(RECIPS)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(SENDER, RECIPS, msg.as_string())
    print 'sendinf image msg..'
    img = make_img_msg('image')
    msg['FROM'] = SENDER
    msg['TO'] = ', '.join(RECIPS)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(SENDER, RECIPS, msg.as_string())


