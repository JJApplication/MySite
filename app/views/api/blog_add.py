# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:51
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_add.py

from . import mypage
from . import api_ajax_blog_add
from app.models import Blog
from flask import jsonify,request
from utils import check_code
from app import db

@mypage.route(api_ajax_blog_add, methods=["post"])
def blog_add():
    try:
        code = request.json["code"]
        if check_code(code):
            title = request.json["title"]
            url = request.json["url"]
            content = request.json["content"]
            try:
                b = Blog(title=title,url=url,content=content)
                db.session.add(b)
                db.session.commit()
                return "ok"
            except:
                db.session.rollback()
                return "bad"
        else:
            return "access denied"

    except:
        return "bad return"