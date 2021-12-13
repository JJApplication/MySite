# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:39
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: console.py

from . import mypage
from . import api_console
from flask import render_template

@mypage.route(api_console)
def console():

    return render_template("console/console.html")