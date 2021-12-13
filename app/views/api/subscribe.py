# -*- coding: utf-8 -*-
# Time: 2020-08-17 0:13
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: subscribe.py

from . import mypage
from . import api_ajax_subscribe
from app.models import Normal,Blog
from flask import jsonify,request
from app import db
import json
from mail_server.task1 import send_blog_mail

@mypage.route(api_ajax_subscribe,methods=["POST"])
def subscribe():
    mail_list = Normal.query.filter_by(key="mail").first()
    if mail_list:
        pass
    else:
        m = Normal(key="mail",value="{}")
        db.session.add(m)
        db.session.commit()
    try:
        mail_list = Normal.query.filter_by(key="mail").first()
        mail = request.json["mail"]
        mail_dict = json.loads(mail_list.value,encoding="utf-8")
        posts = Blog.query.order_by(Blog.id.desc()).limit(5).all()
        t = []
        for p in posts:
            t.append(p.pr())

        if mail in mail_dict.keys():
            send_blog_mail.apply_async([mail,t],countdown=60, retry=False)
            return "repeat"

        else:
            opt = send_blog_mail.apply_async([mail,t], retry=False)
            if opt:
                mail_dict[mail] = mail
                mail_list.value = json.dumps(mail_dict,ensure_ascii=False)
                db.session.commit()
                return "ok"
            else:
                return "bad"
    except Exception as e:
        return "bad"
