# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:41
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_update.py

from . import mypage
from . import api_console_blog_update
from flask import render_template

@mypage.route(api_console_blog_update)
def console_blog_update():

    return render_template("console/blog_update.html")