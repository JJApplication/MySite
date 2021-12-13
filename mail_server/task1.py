# -*- coding: utf-8 -*-
# Time: 2020-08-17 21:33
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: task1.py
from mail_server import celery
from mail_server import *
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import time
import jinja2

@celery.task
def send_blog_mail(address,posts):
    to = address
    try:
        link = "http://renj.io/api/unsub?address=" + address
        html = render_template("mail/blog_sub.html",posts=posts,link=link)
        mail_msg = MIMEText(html,"html","utf-8")
        mail_msg['From'] = sender
        mail_msg['To'] = address
        subject = 'Renj.io Bot'
        mail_msg['Subject'] = Header(subject, 'utf-8')

        server = smtplib.SMTP_SSL(host, port)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, passwd)
        server.sendmail(sender,[to],mail_msg.as_string())
        server.quit()

    except Exception as e:
        #文件日志
        print(e.args)
        t = time.strftime('%Y-%D',time.localtime())
        with open('/home/web/mail.log','a+',encoding='utf-8')as f:
            data = 'address: {}\ntime: {}\nerror: {}\n'.format(address,t,str(e.args))
            f.write(data)
            f.close()

def render_template(template_name, **context):
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('app', 'templates')
    )
    template = env.get_template(template_name)
    return template.render(**context)