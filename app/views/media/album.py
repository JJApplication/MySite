# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:24
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: album.py

from  . import mypage
from . import api_album
from app.models import Album
from flask import render_template

@mypage.route(api_album)
def album():
    photos = Album.query.all()
    return render_template('album.html',photos=photos)