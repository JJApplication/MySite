# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:17
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: home_zan.py

from . import mypage
from . import api_zan
from app.models import Zan
from flask import render_template,redirect,request,url_for
from app import db

@mypage.route(api_zan, methods=['POST'])
def zan():
    if request.method == 'POST':
        realcount = Zan().query.first()
        count = realcount.count
        realcount.count = count + 1
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e.args)

        return str(realcount.count)
    return "null"

