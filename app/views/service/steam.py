# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:21
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: steam.py

from . import mypage
from . import api_steam
from flask import redirect

@mypage.route(api_steam)
def play_steam():

    return redirect("https://steamcommunity.com/id/pipi831143/")