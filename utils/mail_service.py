# -*- coding: utf-8 -*-
# Time: 2020-08-17 0:15
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: mail_service.py

import smtplib
from email.header import Header
from email.mime.text import MIMEText
import time
from flask import current_app,render_template
import threading

def sendmail(address,posts):
    sender = current_app.config["MAIL_USER"]
    passwd = current_app.config["MAIL_PW"]
    host = current_app.config["MAIL_HOST"]
    port = current_app.config["MAIL_PORT"]
    to = address
    try:
        link = "http://renj.io/api/unsub?address=" + address
        html = render_template("blog_sub.html",posts=posts,link=link)
        mail_msg = MIMEText(html,"html","utf-8")
        mail_msg['From'] = sender
        mail_msg['To'] = address
        subject = 'Renj.io博客订阅'
        mail_msg['Subject'] = Header(subject, 'utf-8')

        server = smtplib.SMTP_SSL(host, port)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, passwd)
        server.sendmail(sender,[to],mail_msg.as_string())
        server.quit()
        return True

    except Exception as e:
        #文件日志
        t = time.strftime('%Y-%D',time.localtime())
        with open('/home/web/mail.log','a+',encoding='utf-8')as f:
            data = 'address: {}\ntime: {}\nerror: {}\n'.format(address,t,str(e.args))
            f.write(data)
            f.close()
        return False

# def sendmail(address,posts):
#     mail_t = threading.Thread(target=do,args=(address,posts))
#     mail_t.start()
#     mail_t.join()

