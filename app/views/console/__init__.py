# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:38
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

from .. import mypage
# from app.api import api_console,api_console_blog_add,\
#     api_console_blog_update, api_console_like,api_console_message,\
#     api_console_problems,api_console_thoughts,api_console_album,api_console_views

from app.api.console import *

from .console import console
from .views import console_views
from .like import console_like
from .album import console_album
from .message import console_message
from .problems import console_problems
from .thoughts import console_thoughts
from .blog_add import console_blog_add
from .blog_update import console_blog_update