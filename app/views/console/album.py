# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:44
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: album.py

from . import mypage
from . import api_console_album
from flask import render_template


@mypage.route(api_console_album)
def console_album():

    return render_template("console/album.html")