# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:11
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

from .. import mypage
from app.api.home import *
# from app.api import api_home,api_index,api_mobile,api_english,api_zan,api_about ,\
#     api_mes,api_donate,api_bulletin,api_i,api_album,api_pic,api_videos,api_status,api_proj, \
#     api_public,api_copyright,api_thanks,api_music,api_thoughts,api_timeline

from .home_mobile import home_mobile
from .home_index import home_index
from .home_pc import home_pc
from .home_en import home_en
from .home_i import home_i
from .home_zan import zan

from .about import about
from .bulletin import bulletin
from .copyright import copyright
from .donate import donate
from .message import message
from .music import music
from .project import proj
from .thoughts import thoughts
from .thanks import thanks
from .public import public
from .status import status
from .sitemap import sitemap_page
from .timeline import timeline

from .markdown_filter import markdown_to_html
