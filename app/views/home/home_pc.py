# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:15
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: home_en.py

from . import mypage
from . import api_home
from app.models import Zan,ViewsCount
from flask import render_template

@mypage.route(api_home)
def home_pc():
    realcount = Zan().query.first()
    views = ViewsCount.query.first()

    return render_template('home.html',zancount=realcount.count, views=views.count)