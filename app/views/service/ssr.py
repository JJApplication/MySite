# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: ssr.py

from . import mypage
from . import api_ssr
from flask import render_template
from utils import update

@mypage.route(api_ssr)
def ssr():
    data = update()
    urls = data
    return render_template('ssr.html', urls=urls)