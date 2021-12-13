# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:21
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: home_i.py

from . import mypage
from . import api_i
from app.models import Zan
from flask import render_template,redirect,request,url_for,flash
from app import db

@mypage.route(api_i,methods=['GET', 'POST'])
def home_i():
    realcount = Zan().query.first()
    count = realcount.count
    if request.method == 'POST':
        realcount.count = count + 1
        try:
            db.session.add(realcount)
            db.session.commit()
        except:
            flash('invalid')
        return redirect(url_for('main.i'))
    return render_template('i.html',count=realcount)