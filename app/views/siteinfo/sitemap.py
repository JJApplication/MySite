# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:25
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: sitemap.py

from . import mypage
from . import api_sitemap,api_sitemap2
from flask import send_from_directory

@mypage.route(api_sitemap)
def sitemap():
    return send_from_directory('./static/','{}'.format(api_sitemap).replace("/",""))

@mypage.route(api_sitemap2)
def sitemap2():
    return send_from_directory('./static/','{}'.format(api_sitemap2).replace("/",""))