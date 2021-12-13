# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:19
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: message.py

from . import mypage
from . import api_mes
from app.models import Dbmessage
from flask import render_template,request,flash,redirect,url_for
from app import db

@mypage.route(api_mes, methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        lvmess = request.form.get('mess')
        message = Dbmessage(mess=lvmess)
        try:
            db.session.add(message)
            db.session.commit()
        except:
            flash('invalid')
        return redirect(url_for('mypage.message'))

    mess = reversed(Dbmessage.query.all())

    return render_template('message.html',mess=mess)