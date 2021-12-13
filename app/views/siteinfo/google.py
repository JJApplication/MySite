# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:26
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: google.py

from . import mypage
from . import api_google
from flask import send_from_directory

@mypage.route(api_google)
def google_verify():

    return send_from_directory('./static/','{}'.format(api_google).replace("/",""))