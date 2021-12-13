# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:33
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: copyright.py

from . import mypage
from . import api_copyright
from flask import render_template

@mypage.route(api_copyright)
def copyright():

    return render_template('copyright.html')