# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:29
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: videos_info.py

from . import mypage
from app.api import api_ajax_videos
from flask import request,jsonify
from app.models import Video
from app import db

#暂时用于异步video请求的接口
@mypage.route(api_ajax_videos, methods=['GET','POST'])
def videos_api():
    if request.method == 'POST':
        if not request.json:
            return "bad"
        if request.json.get("like"):
            name = request.json["name"]
            v = Video.query.filter_by(name=name).first()
            if v:
                v.like  += 1
                db.session.commit()
                return "ok"
            else:
                return "bad"

        elif request.json.get("share"):
            name = request.json["name"]
            v = Video.query.filter_by(name=name).first()
            if v:
                v.share  += 1
                db.session.commit()
                return "ok"
            else:
                return "bad"

        elif request.json.get("play"):
            name = request.json["name"]
            v = Video.query.filter_by(name=name).first()
            if v:
                v.play  += 1
                db.session.commit()
                return "ok"
            else:
                return "bad"
        else:
            return ""
    else:
        name = request.args.get("name")
        v = Video.query.filter_by(name=name).first()
        if v:
            return jsonify({"like": v.like,"share": v.share,"play": v.play})
        else:
            return "bad"