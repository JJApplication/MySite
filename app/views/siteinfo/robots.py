# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:25
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: robots.py

from . import mypage
from . import api_robot
from flask import send_from_directory

@mypage.route(api_robot)
def robots():
    return send_from_directory('./static/','{}'.format(api_robot).replace("/",""))