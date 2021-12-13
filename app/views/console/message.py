# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:42
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: message.py

from . import mypage
from . import api_console_message
from flask import render_template
from app.models import Dbmessage

@mypage.route(api_console_message)
def console_message():
    ms = Dbmessage.query.all()
    return render_template("console/message.html",ms=ms)