# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:34
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: thanks.py

from . import mypage
from . import api_thanks
from flask import render_template

@mypage.route(api_thanks)
def thanks():

    return render_template('thanks.html')