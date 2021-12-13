# -*- coding: utf-8 -*-
# Time: 2020-08-10 21:34
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: bing.py

from . import mypage
from . import api_bing
from flask import send_from_directory

@mypage.route(api_bing)
def bing_verify():

    return send_from_directory('./static/','{}'.format(api_bing).replace("/",""))