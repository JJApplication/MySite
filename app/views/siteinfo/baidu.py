# -*- coding: utf-8 -*-
# Time: 2020-08-10 21:33
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: baidu.py

from . import mypage
from . import api_baidu
from flask import send_from_directory

@mypage.route(api_baidu)
def baidu_verify():

    return send_from_directory('./static/','{}'.format(api_baidu).replace("/",""))