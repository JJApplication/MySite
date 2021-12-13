# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:19
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: forest.py

from . import mypage
from . import api_forest
from flask import render_template,redirect,url_for


@mypage.route(api_forest)
def forest():
    return render_template('forest.html',num=30*60)


@mypage.route(api_forest + '/<int:num>s')
def timer(num):
    return render_template('forest.html', num=num)


@mypage.route(api_forest + '/<int:num>m')
def minutes(num):
    return redirect(url_for('mypage.timer', num=num*60))


@mypage.route(api_forest + '/<int:num>h')
def hours(num):
    return redirect(url_for('mypage.timer', num=num*3600))