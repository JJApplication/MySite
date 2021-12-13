# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:59
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: album_add.py


from . import mypage
from . import api_ajax_album_add
from app.models import Album
from flask import jsonify,request
from utils import check_code
from app import db

@mypage.route(api_ajax_album_add, methods=["post"])
def api_add_album():
    try:
        code = request.json["code"]
        if check_code(code):
            year = request.json["year"]
            start = int(request.json["start"])
            count = int(request.json["count"])
            date = request.json["date"]
            info = request.json["info"]
            try:
                for i in range(start,start+count):
                    print("{}-{}.jpg".format(year,i))
                    p = Album(name="{}-{}.jpg".format(year,i),date=date,info=info)
                    db.session.add(p)
                    db.session.commit()
                return "ok"
            except:
                db.session.rollback()
                return "bad"
        else:
            return "access denied"

    except:

        return "bad return"