# -*- coding: utf-8 -*-
# Time: 2020-08-09 18:56
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

# from app.api import api_blog,api_blog_newest,api_blog_sb,api_blog_post,api_blog_page
from .. import mypage
from app.api.blog import *

from .blog_home import blog
from .blog_post import blog_post
from .blog_newst import blog_new_post
from .blog_page import blog_page
from .blog_sb import blog_sb
