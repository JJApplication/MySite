# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:58
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: album_new.py

from . import mypage
from . import api_ajax_album_new
from app.models import Album
from flask import jsonify,request

@mypage.route(api_ajax_album_new, methods=["get"])
def api_get_new_album():
    try:
        key = request.args.get("key")
        if key == '110':
            try:
                n = Album.query.order_by(Album.id.desc()).first()
                return n.name
            except:
                return "bad"
        else:
            return "access denied"

    except:

        return "bad return"
