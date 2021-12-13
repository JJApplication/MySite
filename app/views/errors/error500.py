# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:53
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: 500.py

from flask import render_template
from . import mypage

@mypage.app_errorhandler(500)  # 传入要处理的错误代码
def page_error(e):  # 接受异常对象作为参数
    return render_template('500.html'),500
