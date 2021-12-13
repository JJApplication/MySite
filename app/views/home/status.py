# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:32
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: status.py

from . import mypage
from . import api_status
import datetime,time
from flask import render_template

@mypage.route(api_status)
def status():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    date1 = time.strptime(date, '%Y-%m-%d')
    date2 = '2017-6-22'
    date2 = time.strptime(date2, '%Y-%m-%d')
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    days = str(date1 - date2).replace(', 0:00:00', '')
    year = datetime.datetime.now().strftime('%Y')

    return render_template('status.html',days=days,year=year)