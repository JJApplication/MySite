# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:49
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: like_update.py

from . import mypage
from . import api_ajax_like_update
from app.models import Zan
from flask import jsonify,request
from utils import check_code
from app import db

@mypage.route(api_ajax_like_update,methods=["post"])
def like_update():
    try:
        code = request.json["code"]
        count = int(request.json["like"])
        if check_code(code):
            z = Zan.query.first()
            z.count = count
            try:
                db.session.commit()
                return "ok"
            except:
                db.session.rollback()
                return "bad"
        else:
            return "access denied"
    except:
        return "bad return"