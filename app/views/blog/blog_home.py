# -*- coding: utf-8 -*-
# Time: 2020-08-09 18:57
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_home.py

from . import api_blog
from . import mypage
from app.models import Blog
from utils import generate_list,calcblog
from flask import render_template

@mypage.route(api_blog)
def blog():
    bloglist = Blog.query.order_by(Blog.id.desc()).limit(6).all()
    all = generate_list(Blog.query.all())
    list = generate_list(reversed(bloglist))
    pagelist = calcblog(1,Blog.query.count())
    return render_template('blog.html', data=list,pagelist=pagelist,n=1,nbefore=1,nafter=2,se=all)
