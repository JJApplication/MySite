# -*- coding: utf-8 -*-
# Time: 2020-08-09 17:50
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: develop.py

from . import mypage
# from running_data import bloglist,musiclist,problemslist,thoughtslist
from db_transfer import *
import json
from app.models import Blog,Zan,Dbmessage,Music,Problems,Thoughts,Album,ViewsCount,Video
from app import db

#only for test
test = True

#旧数据库文件持久化为json
@mypage.route('/db_transfer',methods=["POST"])
def transfer():
    """
    旧的数据库迁移工作
    全部数据库
    :return:
    """
    if test:
        #blog
        b = Blog.query.all()
        bl = []
        for p in b:
            bl.append({"title": p.title,"url":p.url,"content": p.content})
        with open("db_transfer/blog.py","w",encoding='utf-8')as f:
            f.write("bloglist = \\\n")
            f.write(json.dumps(bl,ensure_ascii=False,indent=2))
            f.close()

        #music
        m = Music.query.all()
        ml = []
        for p in m:
            ml.append({"name": p.name,"id": p.music_id})
        with open("db_transfer/music.py", "w", encoding='utf-8')as f:
            f.write("musiclist = \\\n")
            f.write(json.dumps(ml, ensure_ascii=False, indent=2))
            f.close()

        #thoughts
        t = Thoughts.query.all()
        tl = []
        for p in t:
            tl.append({"day": p.day,"thought": p.thought})
        with open("db_transfer/thoughts.py", "w", encoding='utf-8')as f:
            f.write("thoughtlist = \\\n")
            f.write(json.dumps(tl, ensure_ascii=False, indent=2))
            f.close()

        #problems
        pro = Problems.query.all()
        pl = []
        for p in pro:
            pl.append({"theme": p.theme,"text": p.text})
        with open("db_transfer/problems.py", "w", encoding='utf-8')as f:
            f.write("problemslist = \\\n")
            f.write(json.dumps(pl, ensure_ascii=False, indent=2))
            f.close()

        #album
        a = Album.query.all()
        al = []
        for p in a:
            al.append({"name": p.name,"date": p.date,"info": p.info})
        with open("db_transfer/album.py", "w", encoding='utf-8')as f:
            f.write("albumlist = \\\n")
            f.write(json.dumps(al, ensure_ascii=False, indent=2))
            f.close()

        #video
        videos = Video.query.all()
        videol = []
        for v in videos:
            videol.append({
                "name": v.name,
                "info": v.info,
                "date": v.date,
                "like": v.like,
                "share": v.share,
                "play": v.play
            })
        with open("db_transfer/video.py", "w", encoding='utf-8')as f:
            f.write("videolist = \\\n")
            f.write(json.dumps(videol, ensure_ascii=False, indent=2))
            f.close()

    return "ok"


#文件写入新数据库
@mypage.route('/blog_transfer',methods=["POST"])
def blog_transfer():
    """
    旧的数据库迁移工作
    :return:
    """
    if test:
        for i in bloglist:
            b = Blog(url=i["url"],title=i["title"],content=i["content"])
            db.session.add(b)
            db.session.commit()

    return "ok"

@mypage.route('/zan_transfer',methods=["POST"])
def zan_transfer():
    """
    旧的数据库迁移工作
    :return:
    """
    if test:
        z = Zan(count=123)
        db.session.add(z)
        db.session.commit()

    return "ok"

@mypage.route('/music_transfer',methods=["POST"])
def m_transfer():
    """
    旧的数据库迁移工作
    :return:
    """
    if test:
        for i in musiclist:
            m = Music(name=i["name"],music_id=i["id"])
            db.session.add(m)
            db.session.commit()

    return "ok"

@mypage.route('/thoughts_transfer',methods=["POST"])
def t_transfer():
    """
    旧的数据库迁移工作
    :return:
    """
    if test:
        for i in thoughtlist:
            m = Thoughts(day=i["day"],thought=i["thought"])
            db.session.add(m)
            db.session.commit()

    return "ok"

@mypage.route('/problems_transfer',methods=["POST"])
def p_transfer():
    """
    旧的数据库迁移工作
    :return:
    """
    if test:
        for i in problemslist:
            m = Problems(theme=i["theme"],text=i["text"])
            db.session.add(m)
            db.session.commit()

    return "ok"

@mypage.route('/album_transfer',methods=["POST"])
def al_transfer():
    """
    旧的数据库迁移工作
    :return:
    """
    if test:
        # for i in range(10,23):
        #     a = Album(name="2020-{}.jpg".format(i),date="2020/7",info="好兄弟云南游")
        #     db.session.add(a)
        #     db.session.commit()
        for al in albumlist:
            a = Album(name=al["name"],date=al["date"],info=al["info"])
            db.session.add(a)
            db.session.commit()

    return "ok"

@mypage.route('/views_transfer',methods=["POST"])
def v_transfer():
    """
    旧的数据库迁移工作
    :return:
    """
    if test:
        if ViewsCount.query.first():
            v = ViewsCount.query.first()
            v.count = 4596
            db.session.commit()
        else:
            v = ViewsCount(view='all',count=4596)
            db.session.add(v)
            db.session.commit()

    return "ok"


@mypage.route('/message_transfer',methods=["POST"])
def me_transfer():
    """
    旧的数据库迁移工作
    :return:
    """
    if test:
        for me in messagelist:
            m = Dbmessage(mess=me)
            db.session.add(m)
            db.session.commit()

    return "ok"

@mypage.route('/video_transfer',methods=["POST"])
def video_transfer():
    """
    旧的数据库迁移工作
    :return:
    """
    cmd = "ffmpeg -y -i abc.mp4 -vcodec copy -acodec copy -vbsf h264_mp4toannexb abc.ts"
    cmd2 = "ffmpeg -i abc.ts -c copy -map 0 -f segment -segment_list playlist.m3u8 -segment_time 5 abc%03d.ts"
    if test:
        for video in videolist:
            v = Video(
                name=video["name"],
                date=video["date"],
                info=video["info"],
                like=video["like"],
                play=video["play"],
                share=video["share"]
            )
            db.session.add(v)
            db.session.commit()

    return "ok"

@mypage.route("/add_bot",methods=["POST"])
def add_bot():
    try:
        googlebot = ViewsCount(view="Googlebot",count=0)
        db.session.add(googlebot)

        baidu = ViewsCount(view="Baiduspider",count=0)
        db.session.add(baidu)

        bingbot = ViewsCount(view="bingbot",count=0)
        db.session.add(bingbot)

        Trident = ViewsCount(view="Trident",count=0)
        db.session.add(Trident)

        Sougou = ViewsCount(view="Sougou",count=0)
        db.session.add(Sougou)

        YandexBot = ViewsCount(view="YandexBot",count=0)
        db.session.add(YandexBot)

        db.session.commit()
        return "ok"
    except:
        db.session.rollback()
        return "bad"

