# -*- coding: utf-8 -*-
# Time: 2020-08-09 20:01
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: login.py

from . import mypage
from flask import render_template
from flask import url_for
from flask_login import login_user,UserMixin,current_user,login_required
from flask import request,flash,redirect
from app import login_manager
from . import api_login

users = [
    {'id':'wzx', 'username': 'wzx', 'password': 'wzx'},
    {'id':'zkh', 'username': 'zkh', 'password': 'zkh'},
    {'id':'zrh', 'username': 'zrh', 'password': 'zrh'},
    {'id':'lrj', 'username': 'lrj', 'password': 'lrj'},
    {'id':'wzj', 'username': 'wzj', 'password': 'wzj'},
]


@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    for user in users:
        if user_id == user['id']:
            # user = User()
            #不使用数据库直接使用全局字典
            # user.id = user_id
            class U(UserMixin):
                pass
            u = U()
            u.id = user_id
            return u #返回用户对象

@mypage.route(api_login, methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #简化密码存储
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('🦐输你🐎呢，爬🐢')
            return redirect(url_for('mypage.login'))

        user = {'id': 'null', 'username': 'null', 'password': 'null'}
        for queryuser in users:
            if username == queryuser["id"]:
                user = queryuser

        # 验证用户名和密码是否一致
        if username == user['username'] and password == user['password']:
            # loguser = User()
            # loguser.id = user['id']
            class U(UserMixin):
                pass
            loguser = U()
            loguser.id = user['id']
            login_user(loguser)  # 登入用户
            flash('Login success.')
            return redirect(url_for('mypage.logged'))  # 重定向到主页
        else:
            flash('Invalid username or password.')  # 如果验证失败，显示错误消息
            return redirect(url_for('mypage.login'))  # 重定向回登录页面

    return render_template('login.html')