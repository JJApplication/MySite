# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:08
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: blog_page.py

from . import api_blog_page
from . import mypage
from app.models import Blog
from utils import generate_list,calcblog
from flask import render_template


@mypage.route(api_blog_page + '/<int:num>')
def blog_page(num):
    bloglist = generate_list(Blog.query.all())
    list = bloglist[(num-1)*7:num*7-1]
    pagelist = calcblog(num ,Blog.query.count())
    nbefore = nafter = 1
    if num == 1:
        nbefore = 1
        nafter = 2
    elif num == pagelist[4]:
        nafter = pagelist[4]
        nbefore = num-1
    else:
        nbefore = num-1
        nafter = num+1

    return render_template('blog.html', data=list,pagelist=pagelist,n=num,nbefore=nbefore,nafter=nafter,se=bloglist)