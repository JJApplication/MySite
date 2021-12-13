# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:14
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: home_index.py

from . import mypage
from . import api_index
from app.models import Zan,ViewsCount
from flask import render_template

@mypage.route(api_index)
def home_index():
    realcount = Zan().query.first()
    views = ViewsCount.query.first()
    return render_template('index.html',zancount=realcount.count, views=views.count)