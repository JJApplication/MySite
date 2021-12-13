# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:21
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: bulletin.py

from . import mypage
from . import api_bulletin
from flask import render_template

@mypage.route(api_bulletin)
def bulletin():

    return render_template('bulletin.html')