# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:40
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_add.py

from . import mypage
from . import api_console_blog_add
from flask import render_template

@mypage.route(api_console_blog_add)
def console_blog_add():

    return render_template("console/blog_add.html")