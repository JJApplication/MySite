# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:06
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_newst.py

from . import api_blog_newest
from . import mypage
from app.models import Blog
from utils import generate_list,calcblog
from flask import render_template,redirect,url_for


@mypage.route(api_blog_newest)
def blog_new_post():
    new = Blog.query.order_by(Blog.id.desc()).first()
    newblog =new.url.replace('/','')

    return redirect(url_for('mypage.blog_post',name=newblog))