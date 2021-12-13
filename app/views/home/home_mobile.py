# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:12
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: home_mobile.py

from . import mypage
from . import api_mobile
from app.models import Zan,ViewsCount,Blog
from flask import render_template

@mypage.route(api_mobile)
def home_mobile():
    realcount = Zan().query.first()
    count = realcount.count
    blogindex = Blog.query.count()
    views = ViewsCount.query.first()
    return render_template('mobile.html',count=count,blogindex=blogindex, views=views.count)