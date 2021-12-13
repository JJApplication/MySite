# -*- coding: utf-8 -*-
# Time: 2020-08-02 18:29
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.config import Config, DevelopConfig

login_manager = LoginManager()  # 实例化扩展类
db = SQLAlchemy()

def create_app(dev=None):

    limiter = Limiter(key_func=get_remote_address,
                      default_limits=['2000/day', '500/hour', '40/5seconds'])
    app = Flask(__name__)

    if dev == 'dev':
        app.config.from_object(DevelopConfig)
    else:
        app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)
    limiter.init_app(app)

    from .views import mypage
    app.register_blueprint(mypage)

    return app
