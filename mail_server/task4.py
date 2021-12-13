# -*- coding: utf-8 -*-
# Time: 2020-08-18 0:21
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: task4.py

# -*- coding: utf-8 -*-
# Time: 2020-08-17 21:45
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: task3.py

#验证码服务
from mail_server import *
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import jinja2

@celery.task
def send_mgek_mail(address):
    to = address
    try:
        html = render_template("mail/mgek.html")
        mail_msg = MIMEText(html,"html","utf-8")
        mail_msg['From'] = sender
        mail_msg['To'] = address
        subject = '订阅Mgek Renj.io Bot'
        mail_msg['Subject'] = Header(subject, 'utf-8')

        server = smtplib.SMTP_SSL(host, port)
        server.login(sender, passwd)
        server.sendmail(sender,[to],mail_msg.as_string())
        server.quit()

    except Exception as e:
        #文件日志
        print(e.args)

def render_template(template_name, **context):
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('app', 'templates')
    )
    template = env.get_template(template_name)
    return template.render(**context)
