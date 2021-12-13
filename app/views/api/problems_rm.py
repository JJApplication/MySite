# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:55
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: problems_rm.py

from . import mypage
from . import api_ajax_problems
from app.models import Problems
from flask import jsonify,request
from utils import check_code
from app import db


@mypage.route(api_ajax_problems + '_rm', methods=["post"])
def rm_problems():
    try:
        code = request.json["code"]
        if check_code(code):
            text = request.json["text"]
            try:
                p = Problems.query.filter_by(text=text).first()
                db.session.delete(p)
                db.session.commit()
                return "ok"
            except:
                db.session.rollback()
                return "bad"
        else:
            return "access denied"

    except:

        return "bad return"