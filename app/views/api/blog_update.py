# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:51
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_update.py

from . import mypage
from . import api_ajax_blog_update
from app.models import Blog, Post
from flask import jsonify,request
from utils import check_code
from app import db
from utils import read_md,blog_content,blog_title,blog_date,tag

@mypage.route(api_ajax_blog_update, methods=["post"])
def blog_update():
    try:
        code = request.json["code"]
        if check_code(code):
            title = request.json["title"]
            url = request.json["url"]
            url2 = request.json["url2"]
            #默认根据url查找并更新,现在如果要修改url就写入url2
            content = request.json["content"]
            url = url if not url.endswith("/") else url.replace("/","")
            b = Blog.query.filter_by(url=url).first()
            if b:
                # 优先判断是不是更新文章操作
                if url and not title and not url2 and not content and Post.query.filter_by(url=url).first():
                    p = Post.query.filter_by(url=url).first()
                    content = read_md('post/' + url.replace('/', '') + '.md')
                    post = blog_content(content)
                    title = blog_title(content)
                    date = blog_date(content)
                    tags = tag(content)

                    try:
                        tags2str = ",".join(tags).strip()
                        p.title = title
                        p.date  = date
                        p.url = url
                        p.post = post
                        p.tags = tags2str

                        db.session.commit()
                        return "ok"
                    except:
                        db.session.rollback()
                        return "bad"
                else:
                    b.url = url2 if url2 != '' else b.url
                    b.title = title if title != '' else b.title
                    b.content = content if content != '' else b.content
                    try:
                        db.session.commit()
                        return "ok"
                    except:
                        db.session.rollback()
                        return "bad"
            else:
                return "not exist"

        else:
            return "access denied"

    except:
        return "bad return"