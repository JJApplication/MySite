# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:02
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: logged.py

from . import mypage
from flask import render_template
from flask import url_for
from flask_login import login_required
from . import api_logged


@mypage.route(api_logged)
@login_required
def logged():
    # return '没有用户需求'
    # return redirect(url_for('main.sb'))

    return render_template('logged.html')