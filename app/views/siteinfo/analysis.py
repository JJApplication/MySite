# -*- coding: utf-8 -*-
# Time: 2020-08-10 15:11
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: analysis.py

from . import mypage
from . import api_analysis
from flask import render_template
from app.models import *

@mypage.route(api_analysis)
def analysis():
    blog_count = Blog.query.count()
    like_count = Zan.query.first().count
    message_count = Dbmessage.query.count()
    album_count = Album.query.count()
    video_count = Video.query.count()
    music_count = Music.query.count()
    thoughts_count = Thoughts.query.count()
    problems_count = Problems.query.count()
    view_count = ViewsCount.query.first().count

    video_like = 0
    video_play = 0
    video = Video.query.all()
    for v in video:
        video_like += v.like
        video_play += v.play

    service_count = 4
    overview = [
        {"name": "blog count","data": blog_count},
        {"name":"like count","data": like_count},
        {"name":"messages","data":message_count},
        {"name":"album count","data":album_count},
        {"name":"video count","data": video_count},
        {"name": "video likes", "data": video_like},
        {"name": "video plays", "data": video_play},
        {"name":"musics","data": music_count},
        {"name":"thoughts","data": thoughts_count},
        {"name":"problems","data": problems_count},
        {"name":"site views","data":view_count},
        {"name":"services","data":service_count}
    ]

    crawlers = ViewsCount.query.all()[1:]
    return render_template("analysis.html",overview=overview,crawlers=crawlers)