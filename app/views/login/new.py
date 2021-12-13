# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:04
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: new.py

from . import mypage
from . import api_new


@mypage.route(api_new)
def new():
    return '暂停用户注册了哦'