# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:55
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: views_count.py


from . import mypage
from app.models import ViewsCount
from app import db
import time
from flask import current_app,request

cache = 0
time_pass = None
@mypage.before_request
def views_count():
    global cache,time_pass
    request_time = time.time()
    if time_pass:
        #存在上一个时间点
        if request_time - time_pass < current_app.config["MAX_VIEW_EXPIRES"]:
            if '/api/' in request.url:
                pass
            elif 'robots.txt' in request.url or 'sitemap.xml' in request.url:
                pass
            elif '/console' in request.url:
                pass
            elif '/static/' in request.url:
                pass
            else:
                cache += 1

        else:
            try:
                d = ViewsCount.query.first()
                d.count += cache
                db.session.commit()
                cache = 0
                time_pass = request_time
            except:
                db.session.rollback()
    else:
        #不存在则更新一个值
        time_pass = request_time
        cache += 1
