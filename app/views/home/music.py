# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:35
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: music.py

from . import mypage
from . import api_music
from app.models import Music
from flask import render_template
from utils import get_list

@mypage.route(api_music)
def music():
    musiclist = get_list(Music.query.all())

    return render_template('music.html',list=musiclist)