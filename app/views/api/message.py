# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:53
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: message.py

from . import mypage
from . import api_ajax_message
from app.models import Dbmessage
from flask import jsonify,request
from utils import check_code
from app import db


@mypage.route(api_ajax_message, methods=["post"])
def message_modify():
    try:
        code = request.json["code"]
        if check_code(code):
            id = int(request.json["id"])
            try:
                m = Dbmessage.query.get(id)
                db.session.delete(m)
                db.session.commit()
                return "ok"
            except:
                db.session.rollback()
                return "bad"
        else:
            return "access denied"

    except:

        return "bad return"