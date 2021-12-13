# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:16
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: home_en.py

from . import mypage
from . import api_english
from app.models import Zan,ViewsCount
from flask import render_template

@mypage.route(api_english)
def home_en():
    realcount = Zan().query.first()
    views = ViewsCount.query.first()
    return render_template('en.html',zan=realcount.count,views=views.count)