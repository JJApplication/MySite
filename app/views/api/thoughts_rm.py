# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:55
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: thoughts_rm.py

from . import mypage
from . import api_ajax_thoughts
from app.models import Thoughts
from flask import jsonify,request
from utils import check_code
from app import db

@mypage.route(api_ajax_thoughts +'_rm', methods=["post"])
def rm_thoughts():
    try:
        code = request.json["code"]
        if check_code(code):
            thought = request.json["thought"]
            try:
                t = Thoughts.query.filter_by(thought=thought).first()
                db.session.delete(t)
                db.session.commit()
                return "ok"
            except:
                db.session.rollback()
                return "bad"
        else:
            return "access denied"

    except:

        return "bad return"