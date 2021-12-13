# -*- coding: utf-8 -*-
# Time: 2020-08-17 15:36
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: chat.py

from . import mypage
from . import api_reply
from flask import render_template

@mypage.route(api_reply)
def reply():

    return render_template("reply.html")