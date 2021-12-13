# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:57
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: ban_crawler.py

from . import mypage
from flask import request,redirect,abort,current_app
from app.models import ViewsCount
from app import db

@mypage.before_request
def ban_crawler():
    referrer = request.referrer
    user_agent = request.user_agent.string

    if current_app.config["DEBUG"]:
        pass
    else:
        if not referrer:
            #判断是否来自本地测试
            check_user_agent(user_agent)
        else:
            #存在referrer 可能是访问内部站点
            if "127.0.0.1" in referrer and "bot" in user_agent:
                abort(403)
            else:
                check_user_agent(user_agent)

def check_user_agent(ua):
    # mapper = {
    #     "Googlebot": "Googlebot",
    #     "Baiduspider": "Baiduspider",
    #     "bingbot": "bingbot",
    #     "Trident": "Trident",
    #     "Sougou web spider": "Sogou",
    #     "YandexBot": "YandexBot"
    # }
    mapper = {
        "googlebot": "Googlebot",
        "baiduspider": "Baiduspider",
        "bingbot": "bingbot",
        "trident": "Trident",
        "sougou web spider": "Sogou",
        "yandexbot": "YandexBot",
        "360spider": "360Spider",
        "yahoo!slurp": "Yahoo!",
        "yisouspider": "Yisou"
    }
    ua = ua.lower()
    all_keys = mapper.keys()
    for key in all_keys:
        if key in ua:
            value = mapper[key]
            cr = ViewsCount.query.filter_by(view=value).first()
            if cr:
                cr.count += 1
                db.session.commit()
                break
            else:
                try:
                    cr = ViewsCount(view=value,count=1)
                    db.session.add(cr)
                    db.session.commit()
                    break
                except:
                    db.session.rollback()
                    break

        else:
            pass
