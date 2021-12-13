# -*- coding: utf-8 -*-
# Time: 2020-08-17 16:10
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: autoreply.py
from . import mypage
from . import api_ajax_reply
from flask import jsonify,request
from mail_server.task2 import send_reply_mail

@mypage.route(api_ajax_reply,methods=["POST"])
def autoreply():
    try:
        mail = request.json["address"]
        try:
            send_reply_mail.apply_async([mail],countdown=10,retry=False)
            return "ok"
        except:
            return "bad"
    except:
        return "bad"
