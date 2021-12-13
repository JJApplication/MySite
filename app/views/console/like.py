# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:41
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: like.py

from . import mypage
from . import api_console_like
from flask import render_template

@mypage.route(api_console_like)
def console_like():

    return render_template("console/like.html")
