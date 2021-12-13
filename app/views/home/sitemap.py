# -*- coding: utf-8 -*-
# Time: 2020-09-09 22:46
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: sitemap.py

from . import mypage
from . import api_sitemap
from flask import render_template

@mypage.route(api_sitemap)
def sitemap_page():
    #有待实现
    return render_template('sitemap.html')