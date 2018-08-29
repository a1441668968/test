from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP

sender = 'd1452823030@163.com'
receiver = 'd1452823030@163.com'
message = MIMEText(_text='这是内容', _charset='utf8')
message['From'] = Header(sender, 'utf8')
message['To'] = Header(receiver, 'utf8')
message['Subject'] = Header('测试邮件', 'utf8')
smtp = SMTP()
smtp.connect('smtp.163.com')
smtp.login('d1452823030', 'zxcv123456')
smtp.sendmail(sender, receiver, message.as_string())
