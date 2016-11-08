import smtplib
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python.','plain', 'utf-8')





sender = 'santiago_young@163.com'
passwd = 'yinxianjun520'
to_who = 'santiago_young@163.com'
smtp_server = 'smtp.163.com'

server = smtplib.SMTP(smtp_server)
server.set_debuglevel(1)
server.login(sender, passwd)
server.sendmail(sender, [to_who], 'hello')
server.quit()












