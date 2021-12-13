# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:42
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: thoughts.py

from . import mypage
from . import api_console_thoughts
from flask import render_template

@mypage.route(api_console_thoughts)
def console_thoughts():

    return render_template("console/thoughts.html")