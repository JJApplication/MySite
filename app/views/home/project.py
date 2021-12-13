# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:32
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: project.py

from . import mypage
from . import api_proj
from flask import render_template

@mypage.route(api_proj)
def proj():

    return render_template("project.html")