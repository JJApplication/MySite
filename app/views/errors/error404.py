# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:51
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: 404.py

from flask import render_template
from . import mypage

@mypage.app_errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'),404# 返回模板和状态码