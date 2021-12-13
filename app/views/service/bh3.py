# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:20
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: bh3.py

from . import mypage
from . import api_bbb
from flask import render_template

@mypage.route(api_bbb)
def play_bbb():

    return render_template('play_bbb.html')