# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:33
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: public.py

from . import mypage
from . import api_public
from flask import render_template

@mypage.route(api_public)
def public():

    return render_template('public.html')