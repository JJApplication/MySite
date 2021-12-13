# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:25
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: pic.py

from  . import mypage
from . import api_pic
from flask import render_template

@mypage.route(api_pic + '/<string:pid>')
def pic(pid):

    return render_template('pic.html',pid=pid)
