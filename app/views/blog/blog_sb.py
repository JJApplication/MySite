# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:05
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_sb.py

from . import api_blog_sb
from . import mypage
from app.models import Blog
from utils import generate_list
from flask import render_template


@mypage.route(api_blog_sb)
def blog_sb():
    pagelist = []
    all = Blog.query.all()
    list = generate_list(all)
    for post in list:
        if "sb" in post["url"]:
            pagelist.append(post)

    return render_template('blog_sb.html', data=pagelist,se=list)