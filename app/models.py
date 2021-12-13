# -*- coding: utf-8 -*-
# Time: 2020-08-02 19:26
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: models.py

from app import db
from flask_login import UserMixin
import time

class Zan(db.Model):  # 表名将会是 dbimg（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    count = db.Column(db.Integer)  # 名字

#用户验证
class User(UserMixin):
    pass

#标准json数据库
class Normal(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    key = db.Column(db.String(50),unique=True)
    value = db.Column(db.TEXT)

#消息数据库
class Dbmessage(db.Model):  # 表名将会是 dbimg（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    mess = db.Column(db.String(250),nullable=False)  # 名字
    time = db.Column(db.String(100),nullable=False)

    def __init__(self,mess):
        self.mess = mess
        self.time = time.strftime("%Y/%m/%d-%H:%M",time.localtime())


class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(50),nullable=False)
    music_id = db.Column(db.String(250),nullable=False)

    def pr(self):
        return {
            "name": self.name,
            "id": self.music_id
        }

class Thoughts(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    day = db.Column(db.String(50),nullable=False)
    thought = db.Column(db.String(250),nullable=False)

    def pr(self):
        return {
            "day": self.day,
            "thought": self.thought
        }


class Problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    theme = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(250), nullable=False)

    def pr(self):
        return {
            "theme": self.theme,
            "text": self.text
        }

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(50), nullable=False,unique=True)
    date = db.Column(db.String(50), nullable=False)
    info = db.Column(db.String(50), nullable=False)
    #添加点赞信息
    like = db.Column(db.Integer,default=0)
    share = db.Column(db.Integer,default=0)

    def pr(self):
        return {
            "name": self.name,
            "date": self.date,
            "info": self.info
        }

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(50), nullable=False,unique=True)
    date = db.Column(db.String(50), nullable=False)
    info = db.Column(db.String(50), nullable=False)
    play = db.Column(db.Integer,default=0) #播放次数
    like = db.Column(db.Integer,default=0) #点赞数
    share = db.Column(db.Integer,default=0) #分享数

    def pr(self):
        return {
            "name": self.name,
            "date": self.date,
            "info": self.info,
            "play": self.play,
            "like": self.like,
            "share": self.share
        }

class ViewsCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    view = db.Column(db.String(50), nullable=False,unique=True)
    count = db.Column(db.Integer, nullable=False)

    def pr(self):
        return {
            "view": self.view,
            "count": self.count,
        }


class Blog(db.Model):
    #因为pin置顶页面 特殊 所以不包含在数据库内部
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120),nullable=False) #标题
    url = db.Column(db.String(50),unique=True,nullable=False) #地址
    content = db.Column(db.TEXT) #摘要

    def __init__(self,title,url:str,content):
        self.title = title
        if url.endswith("/"):
            self.url = url.replace("/","")
        else:
            self.url = url
        self.content = content

    def pr(self):
        return {
            "title": self.title,
            "url": self.url,
            "content": self.content
        }

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120),nullable=False) #标题
    url = db.Column(db.String(50),unique=True,nullable=False) #地址
    post = db.Column(db.TEXT) #正文
    date = db.Column(db.String(20)) #日期
    tags = db.Column(db.String(50)) #标签

    def pr(self):
        return {
            "title": self.title,
            "date": self.date,
            "url": self.url,
            "post": self.post,
            "tags": self.tags
        }