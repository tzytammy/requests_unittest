# -*- coding: utf-8 -*-
'''
From: gh123icdi@126.com
Password: &hui693fight$@
Password: 126gh0
To: 772717473@qq.com
SMTP server: smtp.126.com'''

# 导入相关库
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# 格式化地址
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 接受键盘输入
from_addr = input('From: ')
password = input('Password: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

# 构建发送msg
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 构建发送连接，并发送
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
