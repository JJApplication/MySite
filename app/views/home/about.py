# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: about.py

from . import mypage
from . import api_about
from flask import render_template

@mypage.route(api_about)
def about():
    return render_template('about.html')