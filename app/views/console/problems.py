# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:43
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: problems.py

from . import mypage
from . import api_console_problems
from flask import render_template

@mypage.route(api_console_problems)
def console_problems():

    return render_template("console/problems.html")