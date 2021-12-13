# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:54
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: thoughts.py

from . import mypage
from . import api_ajax_thoughts
from app.models import Thoughts
from flask import jsonify,request
from utils import check_code
from app import db


@mypage.route(api_ajax_thoughts, methods=["post"])
def add_thoughts():
    try:
        code = request.json["code"]
        if check_code(code):
            day = request.json["day"]
            thought = request.json["thought"]
            try:
                t = Thoughts(day=day,thought=thought)
                db.session.add(t)
                db.session.commit()
                return "ok"
            except:
                db.session.rollback()
                return "bad"
        else:
            return "access denied"

    except:

        return "bad return"