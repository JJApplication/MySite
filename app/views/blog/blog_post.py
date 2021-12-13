# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:07
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_post.py

from . import api_blog_post
from . import mypage
from app.models import Post
from utils import read_md,blog_content,blog_title,blog_date,tag
from flask import render_template
from app import db


@mypage.route(api_blog_post + '/<string:name>')
def blog_post(name):
    p = Post.query.filter_by(url=name).first()
    if p:
        title = p.title
        date = p.date
        tags = p.tags.split(",")
        post = p.post
    else:
        #首次获取时同步到数据库
        content = read_md('post/'+ name.replace('/','')+'.md')
        post = blog_content(content)
        title = blog_title(content)
        date = blog_date(content)
        tags = tag(content)

        try:
            tags2str = ",".join(tags).strip()

            p = Post(title=title,date=date,url=name,post=post,tags=tags2str)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()

    return render_template('blog_post.html',name=name,post=post,title=title,date=date,tags=tags)
