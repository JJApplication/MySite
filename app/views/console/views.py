# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:44
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: views.py

from . import mypage
from . import api_console_views
from flask import render_template

@mypage.route(api_console_views)
def console_views():

    return render_template("console/views.html")