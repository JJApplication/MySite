# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:22
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: go.py

from . import mypage
from . import api_go
from flask import render_template
from utils import get_list,getitem
from app.models import Problems


@mypage.route(api_go)
def go():
    data = get_list(Problems.query.all())

    return render_template('go_home.html',problems=data)

@mypage.route(api_go + '/<string:theme>')
def gonext(theme):
    problems = reversed(getitem(theme,get_list(Problems.query.all())))
    if theme =="golang":
        item = "fab fa-github"
    elif theme == "algorithm":
        item = "fas fa-code"
        problems = [{"text": "请跳转至<a href='/book/suanfa/'>算法笔记</a>"}]
    elif theme == "flask":
        item ="fas fa-flask"
    elif theme == "code":
        item = "fab fa-python"
    else:
        item = "fab fa-"+theme

    return render_template('go_page.html',theme=theme,item=item,problems=problems)