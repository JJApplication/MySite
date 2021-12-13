# -*- coding: utf-8 -*-
# Time: 2020-08-17 15:00
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: unsubscribe.py

from . import mypage
from . import api_ajax_unsubscribe
from flask import request
from app.models import Normal
from app import db
import json

@mypage.route(api_ajax_unsubscribe)
def unsubscribe():
    address = request.args.get("address","")
    if address:
        mail_list = Normal.query.filter_by(key="mail").first()
        mail_dict = json.loads(mail_list.value, encoding="utf-8")
        if address in mail_dict.keys():
            del mail_dict[address]
            mail_list.value = json.dumps(mail_dict,ensure_ascii=False)
            db.session.commit()
            return "successfully unsubed"
        else:
            return "mail not exists"
    else:
        return "error"