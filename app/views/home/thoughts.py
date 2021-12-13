# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:34
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: thoughts.py

from . import mypage
from . import api_thoughts
from app.models import Thoughts
from utils import get_list
from flask import render_template


@mypage.route(api_thoughts)
def thoughts():
    data = get_list(Thoughts.query.all())

    return render_template('thoughts.html',datas=data)