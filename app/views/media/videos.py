# -*- coding: utf-8 -*-
# Time: 2020-08-09 19:25
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: videos.py

from  . import mypage
from . import api_videos
from app.models import Video
from flask import render_template,request

@mypage.route(api_videos)
def videos():
    name = request.args.get('watch')
    if name:
        v =  Video.query.filter_by(name=name).first()
        if v:
            return render_template('video.html',video=v)

    videos = Video.query.all()

    return render_template('video_list.html',videos=videos)