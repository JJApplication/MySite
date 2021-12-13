# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:45
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: views_info.py

from . import mypage
from . import api_ajax_views
from app.models import ViewsCount
from flask import jsonify

@mypage.route(api_ajax_views)
def update_views():
    try:
        v = ViewsCount.query.first()
        return jsonify({
            "views": v.count
        })
    except:
        return "None"