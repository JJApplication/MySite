# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:27
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

from .. import mypage
# from app.api import api_ajax_videos,api_ajax_album_add,api_ajax_album_new, \
#     api_ajax_blog_add,api_ajax_blog_update,api_ajax_like_update,api_ajax_views, \
#     api_ajax_message,api_ajax_problems,api_ajax_thoughts,api_ajax_subscribe,api_ajax_unsubscribe,api_ajax_reply

from app.api.ajax import *

from .blog_add import blog_add
from .blog_update import blog_update
from .album_add import api_add_album
from .album_new import api_get_new_album
from .videos_info import videos_api
from .views_info import update_views
from .thoughts import add_thoughts
from .problems import add_problems
from .thoughts_rm import rm_thoughts
from .problems_rm import rm_problems
from .message import message_modify
from .like_update import like_update
from .subscribe import subscribe
from .unsubscribe import unsubscribe
from .autoreply import autoreply
from .mgek_subscribe import mgek_subscribe