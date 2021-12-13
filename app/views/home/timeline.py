# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:35
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: timeline.py

from . import mypage
from . import api_timeline
from flask import render_template

@mypage.route(api_timeline)
def timeline():

    return render_template('timeline.html')