# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:20
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: donate.py

from . import mypage
from . import api_donate
from flask import render_template

@mypage.route(api_donate)
def donate():
    return render_template('donate.html')