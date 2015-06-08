# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'zuo.zhong@163.com'
receiver = '470516189@qq.com'
subject = 'python email test'
smtpServer = 'smtp.163.com'
username = 'zuo.zhong@163.com'
password = 'jik9207177'

msg = MIMEText('你好', 'text', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()


# http://www.cnblogs.com/lonelycatcher/archive/2012/02/09/2343463.html
# http://www.v2ex.com/t/161912
# mailinabox